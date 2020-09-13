from django.shortcuts import render
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import sys
from oauth2client import client
from googleapiclient import sample_tools
from django.db.models import *
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

def fi_post_1(request):
    return render(request, 'fi_post_1.html')

#========================================================house
def ho_post_1(request):
    return render(request, 'ho_post_1.html')

def ho_post_2(request):
    return render(request, 'ho_post_2.html')

def ho_post_3(request):
    return render(request, 'ho_post_3.html')

#========================================================welfare
def wel_post_1(request):
    return render(request, 'wel_post_1.html')

def wel_post_2(request):
    return render(request, 'wel_post_2.html')

def wel_post_3(request):
    return render(request, 'wel_post_3.html')
    
#========================================================

def intro(request):
    return render(request, 'intro.html')

def calendar(request):
    return render(request, 'calendar.html')