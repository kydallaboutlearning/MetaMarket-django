from django.urls import path,include
from django.urls import reverse
from django.contrib.auth import views as auth_views
import django

#importing views
from .views import RegisterView,EditView,LogoutView


#setting proper app name for better url routing
app_name = 'accounts'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('logout_form/user/', LogoutView,name = 'logout_form'),
    path('register/user/',RegisterView,name = 'register'),
    path('edit_profile/', EditView, name = 'edit_profile')
]