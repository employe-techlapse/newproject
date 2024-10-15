from django.urls import path
from .views import get_users, Create_user, user_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', Create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail')
]