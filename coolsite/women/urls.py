from django.urls import path, re_path

from women.views import index, categories, archive, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name = 'about'),
]