from ..models import *
from django import template
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm

register = template.Library()

@register.filter(name = "cook_id")
def find_cook(user_id):
    #sets cook based off my table of USERS/chefs based on the user id
    cook = Users.objects.get(user=user_id)
    return cook.id

@register.filter(name = "changeObjPerm")
def changeObjPerm(user_id, recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)
    user = User.objects.get(id = user_id)
    assign_perm('saved_recipes', user, recipe)
