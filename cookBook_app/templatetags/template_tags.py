from ..models import *
from django import template

register = template.Library()

@register.filter(name = "cook_id")
def find_cook(user_id):
    #sets cook based off my table of USERS/chefs based on the user id
    cook = Users.objects.get(user=user_id)
    return cook.id

