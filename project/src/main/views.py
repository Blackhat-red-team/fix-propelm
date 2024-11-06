# main/views.py
from django.shortcuts import render

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')
def home(request):
    return render(request, 'home.html')  # تأكد من وجود قالب باسم 'home.html' في مجلد templates