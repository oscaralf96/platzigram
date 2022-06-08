from django.urls import path
from . import views
from django.views.generic import TemplateView

from .views import UserDetailView

urlpatterns = [
    path(
        route='view/<str:username>/',
        view=UserDetailView.as_view(template_name='users/detail.html'),
        name='detail'
    ),

    path(
        route='login/',
        view=views.login_view,
        name='login'),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.signup,
        name='signup'),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'),
]

