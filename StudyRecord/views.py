from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    template_name = "../templates/index.html"
    return render(request, template_name)