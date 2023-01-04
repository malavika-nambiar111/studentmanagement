from django.shortcuts import render, redirect
from .models import Courses,Contact,Staff
from django.contrib import messages
# Create your views here.

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email = email,password = password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('newhome')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username or password')
            return redirect('signin')
    return render(request,'signin.html')

def home(request):
    return render(request,'home.html')

def gallery(request):
    return render(request,'gallery.html')

def courses(request):
    dict_courses={
        'courses': Courses.objects.all()
    }
    return render(request,'courses.html',dict_courses)

def form(request):
    return render(request,'form.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dict={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dict)
    return render(request,'contact.html')

def forgot(request):
    return render(request,'forgot.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')