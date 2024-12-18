from django.contrib.auth.models import User



"""Creating the custom backend to authenticate Email"""

class EmailAuthBackend:
    """Authenticating using email"""

    def authenticate(self, request, username = None, password = None ):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
             
            return None          
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None