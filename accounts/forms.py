from django.contrib.auth.forms import (UserCreationForm, 
                                       UserChangeForm)
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    '''Extending the UsercreationForm with the additional field(s) on the CustomUser model.'''
    
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'age',)
        
class CustomUserChangeForm(UserChangeForm):
    '''Extending the UserChangeForm with the additional field(s) on the CustomUser model.'''
    
    class Meta:
        model = User
        fields = ('username', 'email', 'age',)