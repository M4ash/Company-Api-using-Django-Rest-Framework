from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home_page(request):
    #return render(request, 'index.html', myVariables) #can call a variable by {{myVar}} in html
    return HttpResponse("this is homepage")





