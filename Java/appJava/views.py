from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import  HttpResponseNotFound
from django.db.models import Count, Avg, Sum
from appJava.models import *
from django.db.models import Q
import itertools
# Create your views here.
def index(request):
    dato = Usuario.objects.all()
    return render(request, 'index.html',{'dato':dato})
