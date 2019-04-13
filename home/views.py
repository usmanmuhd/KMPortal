from django.shortcuts import render
from .models import Product, ResearchPaper, Design, Requirement
from django.contrib.auth.models import User
import json

def index(request):
    research = User.objects.filter(username=request.user.username, groups__name='Research').exists()
    design = User.objects.filter(username=request.user.username, groups__name='Design').exists()
    man = User.objects.filter(username=request.user.username, groups__name='Manufacturing').exists()
    return render(request, 'main.html', {'research': research, 'design': design, 'man': man})

def products(request):
    research = User.objects.filter(username=request.user.username, groups__name='Research').exists()
    design = User.objects.filter(username=request.user.username, groups__name='Design').exists()
    man = User.objects.filter(username=request.user.username, groups__name='Manufacturing').exists()
    prod = Product.objects.all()
    return render(request, 'products.html', {'prod': prod, 'research': research, 'design': design, 'man': man})

def research(request):
    research = User.objects.filter(username=request.user.username, groups__name='Research').exists()
    print(research)
    paper = ResearchPaper.objects.all()
    return render(request, 'research.html', {'paper': paper, 'research': research})

def designs(request):
    research = User.objects.filter(username=request.user.username, groups__name='Research').exists()
    design = User.objects.filter(username=request.user.username, groups__name='Design').exists()
    prod = Design.objects.all()
    return render(request, 'products.html', {'prod': prod, 'research': research, 'design': design})

def manufacturing(request):
    research = User.objects.filter(username=request.user.username, groups__name='Research').exists()
    design = User.objects.filter(username=request.user.username, groups__name='Design').exists()
    man = User.objects.filter(username=request.user.username, groups__name='Manufacturing').exists()
    req = Requirement.objects.all()
    prod = []
    for i in req:
        a = dict()
        a['picture'] = i.design.picture
        a['name'] = i.design.name
        a['requirements'] = json.loads(i.requirements)
        prod.append(a)
    return render(request, 'man.html', {'prod': prod, 'research': research, 'design': design, 'man': man})
