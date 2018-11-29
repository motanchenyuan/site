from django.shortcuts import render

# Create your views here.
def webtest(request):
  return render(request,'mywebsite/webtest.html',)
  
