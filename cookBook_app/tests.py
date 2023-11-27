from django.test import TestCase,SimpleTestCase
# pages/tests.py
from .models import *
from django.urls import reverse  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.python.org")

print(driver.title)
"""

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "cookBook_app/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>The Cookbook</h1>")
        self.assertNotContains(response, "Not on the page")


class recipesPageTests(SimpleTestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/recipes/")
        self.assertEqual(response.status_code, 200)

"""    def test_url_available_by_name(self):  
        response = self.client.get(reverse("recipes"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("recipes"))
        self.assertTemplateUsed(response, "cookBook_app/recipes_list.html")

    def test_template_content(self):
        response = self.client.get(reverse("recipes"))
        self.assertContains(response, "<h1>Recipes List</h1>")
        self.assertNotContains(response, "Should not be here!")
"""

"""
class recipesDetailViewTest(TestCase):
    def setUp(self):
        # Create a post for testing
        self.post = Recipes.objects.create(title='Test Post', cookTime='This is a test post', difficulty = 'tat', ingredients ='est', recipe ='ateds')

    def test_post_detail_view(self):
        # Test that the recipes detail view returns a 200 status code,
        # uses the correct template, and contains the recipes title
        response = self.client.get(reverse('recipes_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookBook_app/recipes_detail.html')
        self.assertContains(response, 'Test Post')
"""
