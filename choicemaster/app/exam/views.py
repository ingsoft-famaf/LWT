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
            
            # precondicion de que el archivo no sea mayor a X MB (X ~ 50)
            if UploadedFile.size > 419430400:  #si es mayor a 50 lo lee de a chunks de 1MB
                UploadedFile.multiple_chunks(chunk_size=1048576)
            else: #si no los agarra de una
                UploadedFile.read()
            xml_string = ''
            for chunk in chunks:
                xml_string += chunk

            etree.fromstring(xml_string)
        #return render(request,"uploadsuccessful.html")
        return redirect('/home')
    else:
        return redirect('/home')
