from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главаня страница')

def group_posts(request, slug):
    return HttpResponse(f'Страница с постами группы {slug}')
