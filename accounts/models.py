from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.

#setting up the user model
User = get_user_model()


class Question(models.Model):
    question = [
        ('Username', "username"),
        ("Email","email")
    ]
    choice = models.CharField(max_length = 10,choices=question)


class UserProfile(models.Model):
    #setting the user
    User = settings.AUTH_USER_MODEL
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='userprofile')
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank = True)
    pfp = models.ImageField(upload_to = 'user/profile/%Y/%m/%d', blank = True)
    created = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of {self.user.username}"

 

