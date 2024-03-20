from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertAlmostEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplate(response, "home.html")
        
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
