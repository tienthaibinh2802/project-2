from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

def members(request):
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def header(reques):
    mymembers = Member.objects.all().values()
    template = loader.get_template('header.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
