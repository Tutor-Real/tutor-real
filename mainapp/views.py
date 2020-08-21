from django.shortcuts import render

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

def intro(request):
    return render(request, 'intro.html')