from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
# req -> response 
# action

def say_hello(req) :
    x = 1
    y = 2 
    return render(req, 'hello.html', {"name": "Sam"})

def return_json(req) :
    return JsonResponse({"name": "Sam Or", "profilePage": "https://samor1014.github.io/", "linkedin": "https://www.linkedin.com/in/chamsumor/?trk=opento_sprofile_pfeditor"})