from django.urls import path
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    path('signup/', views.signup, name='signup'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
]