from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .schema import VALIDATOR
from lxml import etree

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
                if (xmlschema.validate(doc)):
                    return HttpResponse('buena wn')
                else:
                    return HttpResponse('la tai cagando')
                return redirect('/success/url/')
            else:
                return redirect('/mal/url/')
        else:
            return redirect('/')
    else:
        return redirect('/')
