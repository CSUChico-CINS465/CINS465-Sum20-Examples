from django.test import TestCase
from django.contrib.auth.models import User

from . import models
from . import views


# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        models.SuggestionModel.objects.create(suggestion="lion", author=user)
        models.SuggestionModel.objects.create(suggestion="cat", author=user)

    def test_suggestion_to_string(self):
        lion = models.SuggestionModel.objects.get(suggestion="lion")
        cat = models.SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(str(lion), 'lion - john')
        self.assertEqual(str(cat), 'cat - john')

    def test_suggestion_author(self):
        lion = models.SuggestionModel.objects.get(suggestion="lion")
        cat = models.SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(lion.author.username, "john")
        self.assertEqual(cat.author.username, "john")

    def test_suggestion_suggestion(self):
        lion = models.SuggestionModel.objects.get(suggestion="lion")
        cat = models.SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(lion.suggestion, "lion")
        self.assertEqual(cat.suggestion, "cat")
