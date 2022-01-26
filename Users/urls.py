from django.urls import path

from Users.views import login, logout, signup, verify

app_name = 'users'

urlpatterns = [
    path('users/signup', signup, name='signup'),
    path('users/login', login, name='login'),
    path('users/logout', logout, name='logout'),
    path('users/verify/<str:id>', verify, name='verify')
]


