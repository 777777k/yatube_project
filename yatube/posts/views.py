from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    text = "Это главная страница проекта Yatube"
    title = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = "Здесь будет информация о группах проекта Yatube"
    title = 'Информация о группах'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
