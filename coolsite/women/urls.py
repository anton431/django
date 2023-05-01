from django.urls import path

from women.views import index, categories

urlpatterns = [
    path('', index),
    path('cats/', categories)
]