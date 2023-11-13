from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *
# Create your views here.
def index(request):

    # Render index.html
    return render( request, 'cookBook_app/index.html')

#View that renders the login html for the login request
def loginPage(request):
    context = {}
    return render(request, 'cookBook_app/login.html', context)


#View that renders the register html for the register request
def registerPage(request):
    context = {}
    return render(request, 'cookBook_app/register.html', context)


class UsersListView(generic.ListView):
    model = Users
class UsersDetailView(generic.DetailView):
    model = Users 
    #def get_context_data to send additional variables to template
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context for the current portfolio
        context = super(UsersDetailView, self).get_context_data(**kwargs)
        # Get recipes that use the current User and add it to the context
        context['recipes'] = Recipes.objects.filter(user=context['users'])
        return context


class RecipeListView(generic.ListView):
    model = Recipes
class RecipeDetailView(generic.DetailView):
    model = Recipes 

def createRecipe(request, user_id):

    form = RecipeForm()
    user = Users.objects.get(pk=user_id)
    
    if request.method == 'POST':
        
        form = RecipeForm(request.POST)

        if form.is_valid():
            # Save the form without committing to the database
            recipe = form.save(commit=False)
            # Set the recipe relationship
            recipe.user = user
            recipe.save()

            # Redirect back to the user detail page
            return redirect('user-detail', user_id)

    context = {'form': form}
    return render(request, 'cookBook_app/recipes_form.html', context)

def updateRecipe(request, user_id, id):
    #sets user based on user id of recipe in url
    user = Users.objects.get(pk=user_id)
    #sets the recipe based on the id from the url
    recipe = Recipes.objects.get(id = id)
    #generates a recipe form using the current instance of the recipe
    form = RecipeForm(instance = recipe)
    
    #check the method is as expected
    if request.method == 'POST':
        
        #generates a recipe form using the current instance of the recipe and trys to post the updated information
        form = RecipeForm(request.POST, instance = recipe)

        #if all required values are set then continue
        if form.is_valid():
            # Save the form without committing to the database
            recipe = form.save(commit=False)
            # Set the user relationship
            recipe.user = user
            recipe.save()

            # Redirect back to the recipe detail page
            return redirect('user-detail', user_id)

    #pass in the form as a form in the dictionary so that we can use it in the project_form template
    context = {'form': form}
    #go to recipe_form template with this information
    return render(request, 'cookBook_app/recipes_form.html', context)

#method to delete a recipe for a user
def deleteRecipe(request, user_id, id):

    #sets the recipe based on the id from the url
    recipe = Recipes.objects.get(id = id)

    #check the method is as expected
    if request.method == 'POST':
        #delete the project using funtion delete()
        recipe.delete()
        # Redirect back to the recipes list page
        return redirect('user-detail', user_id)

    #pass in the project as an item in the dictionary because thats what we called it in the delete template
    context = {'item': recipe}
    #go to delete template with this information
    return render(request, 'cookBook_app/delete.html', context)
