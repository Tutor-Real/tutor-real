from django.shortcuts import render
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import sys
from oauth2client import client
from googleapiclient import sample_tools
# pip install google-api-python-client
# pip install oauth2client

# Create your views here.

def main(request):
    return render(request, 'main.html')

def finance(request):
    return render(request, 'finance.html')

def welfare(request):
    return render(request, 'welfare.html')

def house(request):
    return render(request, 'house.html')

def post(request):
    return render(request, 'post.html')

<<<<<<< HEAD
def calendar(request):
    
    return render(request, 'calendar.html')
=======
def intro(request):
    return render(request, 'intro.html')
>>>>>>> 3d5aef819a2d77e30f84f3cf3150af0f304e8daa
