from django.http import HttpResponse
from django.shortcuts import render
from .models import Admin, Register, Packages
from django.contrib import messages
def ttmhome(request):
    return render(request,"ttmhome.html")

def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(username=name, password=pwdd).values()
        if flag:        #flag is not empty
            if name=="Navya":         #Navya is Admin
                messages.info(request,"This is Admin TTM page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is User TTM page")
            return render(request, "ttmhome.html")
        else:
            messages.info(request, "Your credentials Are not Correct")
            return render(request, "loginfail.html")
def checkregistration(request):
    if request.method=="POST":
        name = request.POST["name"]
        addr =  request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname= request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email existing...")
                return render(request,"register.html")
            else:
                user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request,"user created...")
                return render(request,"LoginPage.html")
        else:
            messages.info(request,"password is not matching...")
            return render(request,"register.html")
def checkpackages(request):
    if request.method=="POST":
        tcode=request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack=Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request, "Data Inserted Successfully ")
        return render(request,"package.html")
    else:
        return render(request, "package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})



def checkChangePassword(request):
            if request.method == "POST":
                uname = request.POST["uname"]
                opwd = request.POST["opwd"]
                npwd = request.POST["npwd"]
                flag = Register.objects.filter(username=uname, password=opwd).values()
                if flag:
                    Register.objects.filter(username=uname, password=opwd).update(password=npwd)
                    return render(request, "index.html")
                else:
                    return render(request, "changepassword.html")
            return render(request, "changepassword.html")



