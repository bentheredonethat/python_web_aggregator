from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

def results(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)

def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")
