from django.db import models, connection
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_lenght=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

class QuestionManager(models.Manager):
    def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')
        

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
