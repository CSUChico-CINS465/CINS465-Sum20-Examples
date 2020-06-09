from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.suggestion + " - " + self.author.username

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    suggestion = models.ForeignKey(SuggestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment