from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
class RecipeForm(ModelForm):
    class Meta: 
        model = Recipes
        fields =('title', 'cookTime', 'difficulty', 'ingredients', 'recipe','public')

class CreateUserForm(UserCreationForm):
    model = User
    fields = ['username', 'email', 'password1', 'password2']

