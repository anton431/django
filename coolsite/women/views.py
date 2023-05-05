from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm
from .models import Women, Category

menu = [{'title': 'О сайте','url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title':'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
# def index(request):
#     posts = Women.objects.all()
#     context = {
#         'posts': posts,
#         'cat_selected': 0,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#     return render(request, 'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title':'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form':form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f"Категория - {context['posts'][0].cat}"
        context['cat_selected'] = self.kwargs['cat_slug']
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'])
# def show_category(request, cat_slug):
#     cat_id = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if not posts:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'cat_selected': cat_slug,
#         'menu': menu,
#         'title': 'Отображение по рубрикам'
#     }
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request,  exception):
    return HttpResponse("Страница не найдена")