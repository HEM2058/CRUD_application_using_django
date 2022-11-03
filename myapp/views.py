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


#Edit page view
def EditPage(request,pk):
  #Fetching the data of particular ID
  get_data=Teacher.objects.get(id=pk)
  return render(request,"edit.html",{'key2':get_data})
#Update Data views
def UpdateData(request,pk):
  udate=Teacher.objects.get(id=pk)
  udate.Firstname=request.POST['fname']
  udate.Lastname=request.POST['lname']
  udate.Email=request.POST['email']
  udate.Contact=request.POST['contact']
  #Query for update
  udate.save()
  return redirect('showpage')
#Delete data view
def DeleteData(request,pk):
 ddata=Teacher.objects.get(id=pk)
 #Query for delete
 ddata.delete()
 return redirect('showpage')

  