from django.urls import path
from .views import *
app_name = 'account'
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),
]
