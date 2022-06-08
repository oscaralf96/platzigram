from django.urls import path
from . import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='posts'
     ),
    path(
        route='new/',
        view=views.CreatePostView.as_view(),
        name='create_post'),

]