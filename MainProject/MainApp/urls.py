from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('login/', views.register, name="login"),
    path('register/', views.register, name="register"),
    ##path('about/', views.about, name="about"),
    ##path('menu/', views.menu, name="menu"),
    path('reservation/', views.reservation, name="reservation"),
 #   path('gallery/', views.gallery, name="gallery"),
    path('review/', views.review, name="review"),
    #path('blog/', views.blog, name="blog")
]
