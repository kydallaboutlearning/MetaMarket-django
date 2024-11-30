from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginQuestion,EmailLoginForm, UsernameLoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.

def LoginView(request):
    form = LoginQuestion()
    if request.method == 'POST':

        #adding the login question form
        form = LoginQuestion(request.POST)

        if form.is_valid:#checking if form is valid
            cd = form.changed_data #getting filled form 

            if cd == 'Email':#checking if login is via username
                emailform = EmailLoginForm(request.POST)
                if form.is_valid():
                    cd = emailform.cleaned_data #getting filled form

                    #authenticating user
                    user = authenticate(
                        request,
                        email = cd['email'],
                        password = cd['password']
                    )
                    if user is not None: #checking if user is registered
                        if user.is_active:
                            login(request,user)
                            redirect('shop:product_list')
                        else:
                            return HttpResponse('Disabled account')
                    
                    else:
                        return HttpResponse('Wrong login info')
            elif cd == 'Username':
                usernameform = UsernameLoginForm(request.POST)#getting login form
                cd = usernameform.cleaned_data
                if usernameform.is_valid():
                    user = authenticate(
                        request,
                        username = cd['username'],
                        password = cd['password']
                    )
                    if user is not None:
                        login(request,user)
                        return redirect('shop:product_list')
                    else:
                        return HttpResponse('Wrong login info')
        else:
                form = LoginQuestion()
    else:
        form = LoginQuestion
        return render(request,'account/login.html',{'form':form})  


"""Creating a registration View"""
def RegisterView(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        
        #checking if form filled is valid
        # 
        if user_form.is_valid():
               
               #saving the form but not to the database
               new_user = user_form.save(commit=False)

               #setting created password
               new_user.set_password(user_form.cleaned_data['password'])

               #saving the user object with the set password
               new_user.save()

               # creating a new profile
               Profile = UserProfile.objects.create(user=new_user)
               messages.success(request,
                                f'Congrats {new_user.username},/n Your Account has been created successfully'
                                )

               #return the view and data

               return render(request,
                             'registration/register_done.html',
                             {'new_user':new_user,
                              'user_profile':Profile}
                             )
       

    else:
        user_form = UserRegistrationForm()

    #returning the registration template
    return render(request,
                  'registration/register.html',
                  {'user_form':user_form}
                  )


"""creating  a profile edit view"""
@login_required
def EditView(request):
    user_form = UserEditForm(instance = request.user,data = request.POST)
    profile_form = ProfileEditForm(instance = request.user, data = request.POST, files=request.FILES)

    #determining the nethod of the form
    if request.method == "POST":
        #getting the form to be filled
        user_form = UserEditForm(instance = request.user,data = request.POST)
        profile_form = ProfileEditForm(instance = request.user, data = request.POST, files=request.FILES)

        if user_form.is_valid and profile_form.is_valid :
            user_form = user_form.cleaned_data
            profile_form = profile_form.cleaned_data
            user_form.save()
            profile_form.save()
            messages.success(request,
                             f'Congrats, {request.user.username}, Your profile has be unpdated successfully')
            return redirect('shop:product_list')
    
    else:
        user_form
        profile_form
    return render(request,'registration/profile_editform.html',
                  {'user_form':user_form,
                   'profile_form':profile_form}
                   )

def LogoutView(request):
    return render(request,'registration/logoutform.html')
