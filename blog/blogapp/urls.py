from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('blogdetails/<slug:slug>', views.blogdetails, name='blogdetails'),
    path('about/', views.about, name='about'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]