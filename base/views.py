from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Home.html')


def project_detail(request):
    return render(request, 'project_detail.html')