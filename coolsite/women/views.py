from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Women, Category

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title':'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'cat_selected': 0,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title':'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    cat_id = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat_id)

    if not posts:
        raise Http404()

    context = {
        'posts': posts,
        'cat_selected': cat_slug,
        'menu': menu,
        'title': 'Отображение по рубрикам'
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request,  exception):
    return HttpResponse("Страница не найдена")