from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .schema import VALIDATOR
from lxml import etree
from ..exam.models import Question, Choice
from editdistance import eval
# Create your views here.
@login_required
def Form(request):
    if request.user.is_superuser:
        return render(request, "UploadQuestions.html", {})
    else:
       return redirect('/home')

@login_required
def Parse(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            xml_string = ''
            if form.is_valid():
                if form.cleaned_data['file'].size > 41943040:
                    form.cleaned_data['file'].multiple_chunks(chunk_size=1048576)
                    for chunk in chunks:
                        xml_string += chunk
                else:
                    xml_string = form.cleaned_data['file'].read()
                doc = etree.fromstring(xml_string)
                xmlschema_doc = etree.parse(VALIDATOR)
                xmlschema = etree.XMLSchema(xmlschema_doc)
                if xmlschema.validate(doc):
                    sj_children = list(doc)
                    for tchild in sj_children:
                        if tchild.tag == 'stext':
                            subject = tchild.text
                        else:
                            for qchild in tchild:
                                if qchild.tag == 'ttext':
                                    topic =  qchild.text
                                else:
                                    question = None
                                    q = None
                                    for child in qchild:
                                        if child.tag == 'qtext':
                                            question = child.text
                                        else:
                                            answer = child.text
                                        if question is not None:
                                            ql = Question.objects.all()
                                            duplicated = False
                                            for qeval in ql:
                                                if eval(qeval.question_text, question) < 6:
                                                    duplicated = True
                                            if not duplicated:
                                                q = Question(subject=subject, topic=topic, question_text=question)
                                                q.save()
                                            question = None
                                        elif q is not None:
                                            if child.tag == 'tanswer':
                                                c = Choice(question=q, choice_text=answer, is_correct=True)
                                            else:
                                                c = Choice(question=q, choice_text=answer)
                                            c.save()
                else:
                    return redirect('/upload/something_went_wrong')
                return redirect('/upload/success/')
            else:
                return redirect('/upload/something_went_wrong')
        else:
            return redirect('/')
    else:
        return redirect('/')

def Sth_wrong_admin(request):
    return render(request, 'sth_wrong_admin.html')

def Success(request):
    return render(request, 'xml_success.html')
