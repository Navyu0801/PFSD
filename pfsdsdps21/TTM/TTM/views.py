from django.shortcuts import render


def homePage(request):
    return render(request,'index.html')
def AboutUs(request):
    return render(request,"AboutUs.html")

def LoginPage(request):
    return render(request,"LoginPage.html")

def ContactUs(request):
    return render(request,"ContactUs.html")

def registrationPage(request):
    return render(request,"register.html")