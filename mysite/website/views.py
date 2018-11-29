from django.shortcuts import render

# Create your views here.
def webtest(request):
  return redirect("webtemplate/test.html")
  
