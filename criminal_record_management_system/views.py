from django.shortcuts import render , redirect
from django.http import HttpResponse

def homepage(request):
    return render(request,'homepage.html')

def learnmore(request):
    return render(request, 'learnmore.html')
def getstart(request):
    return render(request, 'getstart.html')