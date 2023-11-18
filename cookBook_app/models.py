from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.

class Users (models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)

    #Define default String to return the name for representing the Model object.
    def __str__(self):
        return self.name
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])
    

class Recipes(models.Model):
    title = models.CharField(max_length=200, blank = False)
    cookTime = models.CharField(max_length=200, blank = True)
    difficulty = models.CharField(max_length=200, blank = True)
    ingredients = models.TextField(blank = False)
    recipe = models.TextField(blank = False)
    public= models.BooleanField(default = False)
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, default = None)

    #Define default String to return the title for representing the Model object.
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("recipe-detail",  args=[str(self.id)])