from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"message":"This tag is rendered from views file from Django directory"})

def date(request):
    return HttpResponse(f"Time is {datetime.now()}")

def about(request):
    return HttpResponse('I am Sajith')