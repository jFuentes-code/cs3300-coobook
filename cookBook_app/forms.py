from django.forms import ModelForm
from .models import *


#create class for project form
class RecipeForm(ModelForm):
    class Meta: 
        model = Recipes
        fields =('title', 'cookTime', 'difficulty', 'ingredients', 'recipe','public')

