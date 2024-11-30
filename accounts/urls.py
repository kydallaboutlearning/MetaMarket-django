from django.urls import path,include
from django.urls import reverse
from django.contrib.auth import views as auth_views
import django
#importing gettextlazy for translation
from django.utils.translation import gettext_lazy as _


#importing views
from .views import RegisterView,EditView,LogoutView


#setting proper app name for better url routing
app_name = 'accounts'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path(_('logout_form/user/'), LogoutView,name = 'logout_form'),
    path(_('register/user/'),RegisterView,name = 'register'),
    path(_('edit_profile/'), EditView, name = 'edit_profile')
]