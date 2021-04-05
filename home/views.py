from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.core.files.storage import FileSystemStorage
from home.models import Crackels_mod


# Create your views here.
def home(request):
    return render(request,'index.html')
def base(request):
	return render(request,'home.html')
def signup(request):
	return render(request,'signup.html')
def crackles(request):
    Sql_data= Crackels_mod.objects.all()

    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        firstname1 = request.POST['firstname1']
        lastname1 = request.POST['lastname1']
        # inputGroupFile02 = request.POST['inputGroupFile02']
        PFT_Location = request.POST['PFT_Location']
        AudioFile = request.FILES['AudioFile']
        fs = FileSystemStorage()
        fs.save(AudioFile.name, AudioFile)
        PFT_image = request.POST['PFT_image']
        f = FileSystemStorage()
        f.save(PFT_image.name,PFT_image)
        Comment_box = request.POST['Comment_box']
        Crackels = Crackels_mod(patient_id = patient_id,firstname1=firstname1,lastname1 = lastname1,PFT_Location=PFT_Location,AudioFile=AudioFile,PFT_image =PFT_image ,Comment_box=Comment_box)
        Crackels.save()
        return render(request,'crackles.html')

    else:
        context= {"Sql_data": Sql_data}
        messages.success(request,"Successfully Added ")
        return render(request,'crackles.html',context)
def wheezes(request):
    return render(request,'wheezes.html')
def crackles_wheezes(request):
    return render(request,'crac_whee.html')
def stirdor(request):
    return render(request,'stirdor.html')
def squawks(request):
    return render(request,'squawks.html')
def sounds(request):
    return render(request,'sounds.html')
def disease(request):
    return render(request,'disease.html')
def references(request):
    return render(request,'references.html')
def contacts(request):
    return render(request,'contacts.html')
def review(request):
    return render(request,'review.html')
def crackles_sound(request):
    return render(request,'crackles_sound.html')
def crackleswheezes_sound(request):
    return render(request,'crackleswheezes_sound.html')
def wheezes_sound(request):
    return render(request,'wheezes_sound.html')
def stirdor_sound(request):
    return render(request,'stirdor_sound.html')
def squawks_sound(request):
    return render(request,'squawks_sound.html')
def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #cheks for error
        if len(username) > 10:
            messages.success(request,"Username must not be more than 10 words ")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your accound has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername,password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Loggedin")
            return redirect('/base')

        else:
            messages.success(request,'invalid user')
            return redirect('/')

def handleLogout(request):
        logout(request)
        messages.success(request,"successfully Loggedout")
        return redirect('/')
