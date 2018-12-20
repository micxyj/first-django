from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('button/', views.button, name='button'),
    path('hello/', views.page_one, name='index1'),
    path('world/', views.page_two, name='index2'),
]