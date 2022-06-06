from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='posts'),
    path('new/', views.create_post, name='create_post'),

]