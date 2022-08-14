from django.urls import path

from . import views

urlpatterns = [
    path('a/a/', views.index),
    path('', views.myfirstfunc),
]
