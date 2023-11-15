from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.models import Group
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):

    # Render index.html
    return render( request, 'cookBook_app/index.html')


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user_role'])
def userPage(request):
    user_id = request.user.id
    cook = Users.objects.get(user=user_id)
    form = UsersForm(instance = cook)
    print('cook', cook)

    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance = cook)
        if form.is_valid():
            
            form.save()
    
    context = {'cook':cook,'form':form}
    return render(request, 'cookBook_app/user.html', context)



#View that renders the register html for the register request
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'user_role')
            user.groups.add(group)
            cook = Users.objects.create(user = user,)
            cook.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


class UsersListView(LoginRequiredMixin,generic.ListView):
    model = Users
class UsersDetailView(LoginRequiredMixin,generic.DetailView):
    model = Users 
    #def get_context_data to send additional variables to template
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context for the current portfolio
        context = super(UsersDetailView, self).get_context_data(**kwargs)
        # Get recipes that use the current User and add it to the context
        context['recipes'] = Recipes.objects.filter(user=context['users'])
        return context


class RecipeListView(LoginRequiredMixin,generic.ListView):
    model = Recipes
class RecipeDetailView(LoginRequiredMixin,generic.DetailView):
    model = Recipes 


@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user_role'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user_role'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['user_role'])
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
