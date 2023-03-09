from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return HttpResponse('mumbai indians captain')
def bumrah(request):
    return HttpResponse('he is no1 bowler in the world')
