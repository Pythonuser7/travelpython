from. import views
from django.urls import path

urlpatterns = [
    path('', views.demo1, name='demo1'),
    path('about/', views.about, name='about')
]
