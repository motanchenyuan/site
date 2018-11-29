from django.shortcuts import HttpResponse, render, redirect
# Create your views here.
def webtest(request):
  return render(request,"test.html")
  
