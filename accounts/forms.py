from django import forms
from django.contrib.auth import get_user_model
from .models import Question,UserProfile
from django.conf import settings


User = get_user_model()
class UsernameLoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 50,required = True, widget=forms.PasswordInput)


class EmailLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length = 50,required=True,widget=forms.PasswordInput)

class LoginQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'choice'
        ]


"""Creating A registration form"""
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email']
    

    password = forms.CharField(max_length = 100,label = 'Password' ,widget = forms.PasswordInput)
    password2 = forms.CharField(max_length = 200,label = 'Repeat Password',widget = forms.PasswordInput)

    
    def clean_password2(self):
        data = self.cleaned_data #getting cleaned data

        #checking if filled password match then raise a validation error
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords Does'nt match, Try again")
        
        return data['password2']
    
    def clean_email(self):
        data = self.cleaned_data
        if User.objects.filter(email=data['email']).exists():
            raise forms.ValidationError('Email already in use ')
        return data['email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number','date_of_birth','pfp', ]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields  = ['username', 'email', 'first_name','last_name']

    #cleaning email for validation
    def clean_email(self):
        data = self.cleaned_data['email']
        #Excluding user email
        existing_email = User.objects.exclude(id=self.instance.id).filter(email=data)
        if existing_email.exists():

            #raising Validation Error
            return forms.ValidationError('Email already in use')
        #returning data if email is valid
        return data
   