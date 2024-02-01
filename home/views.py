from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
  
  peoples=[
    {'name':'Vedant','age':'21'},
    {'name':'Vaisu','age':'30'},
    {'name':'Nikki','age':'15'}
  ]
  return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
  context={'title':"About Page for website"}
  return HttpResponse("<h2>Success!</h2>")

def about(request):
  context={'title':"About Page for website"}
  return render(request,"about.html",context)

def contact(request):
  context={'title':"Contact Page for website"}
  return render(request,"contact.html")