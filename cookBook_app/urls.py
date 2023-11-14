from django.urls import path, include
from . import views



urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

#Update urls.py to include path to list and detail views
path('users/', views.UsersListView.as_view(), name= 'users'),
path('user/<int:pk>', views.UsersDetailView.as_view(), name='user-detail'),
path('recipes/', views.RecipeListView.as_view(), name= 'recipes'),
path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),

#url for recipe creation that takes in user id
path('users/<int:user_id>/create_recipe/', views.createRecipe, name='create_recipe'),
#url for updating a recipe that takes in user id and recipe id
path('users/<int:user_id>/update_recipe/<int:id>', views.updateRecipe, name='update_recipe'),
#url for recipe deletion that takes in user id and recipe id
path('users/<int:user_id>/delete_recipe/<int:id>', views.deleteRecipe, name='delete_recipe'),

#login/registration urls
path('accounts/', include('django.contrib.auth.urls')),

path('accounts/register/', views.registerPage, name = "register_page"),




]
