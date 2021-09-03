from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog-detail/<int:pk>/', views.detail, name='blog_detail'),
    path('payment/', views.payment, name='payment'),
    path('result/', views.result, name='result'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('subscribe/', views.subscribe, name='subscribe'),
]