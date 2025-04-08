from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')


def sign_detect(request):
    return render(request, 'main/sign_detect.html')


def registration(request):
    return render(request, 'main/registration.html')