from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InserPageView(request):
    return render(request,"insert.html")

def InsertData(request):
    #Data come from html to views
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    #creating object of Model class
    #Inserting Data into Table

    newuser=Teacher.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    #After insert render on Show.html
    # return render(request,"show.html")
    #After Insert render pn ShowPsge view
    return redirect('showpage')
  #showpage view
def ShowPage(request):
    #select * from tablename
    #For fetching all the data of table
    all_data=Teacher.objects.all()
    return render(request,"show.html",{'key1':all_data})



  