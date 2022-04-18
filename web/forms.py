# from pyexpat import model
# from attr import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']