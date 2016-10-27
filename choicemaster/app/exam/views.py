from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Form(request):
    if request.user.is_superuser:
        return render(request, "UploadQuestions.html", {})
    else:
       return redirect('/home')

@login_required
def Upload(request):
    if request.user.is_superuser:
        for count, x in enumerate(request.FILES.getlist("files")):
            def process(f):
                with open('/home/juan/ingsoft/LWT/choicemaster/media/file_' + str(count), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            process(x)
        #return render(request,"uploadsuccessful.html")
        return redirect('/home')
    else:
        return redirect('/home')
