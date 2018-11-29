from django.shortcuts import HttpResponse, render, redirect
# Create your views here.
def webtest(request):
  return redirect("webtemplate/test.html")
  
