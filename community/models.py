from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

# This is for the timestamp that defines when a question has been added
# It will return a string like:
    # '2 days ago', '20 seconds ago' and so on...
def x_ago_helper(diff):
    if diff.days > 0:
        if diff.days == 1:
            return f'{diff.days} day ago'
        else:
            return f'{diff.days} days ago'
    if diff.seconds < 60:
        if diff.seconds == 1:
            return f'{diff.seconds} second ago'
        else:
            return f'{diff.seconds} seconds ago'
    if diff.seconds < 3600:
        return f'{diff.seconds // 60} minutes ago'
    return f'{diff.seconds // 3600} hours ago'



class Question(models.Model):
    """A Question the user want to ask"""
    question = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        """Return a string representation of the model."""
        return self.question

    def get_absolute_url(self):
       return reverse('community:index')
    

    @property
    def num_answers(self):
        answers = Answer.objects.filter(question_id = self.id)
        return len(answers)

    def x_ago(self):
        diff = timezone.now() - self.pub_date
        return x_ago_helper(diff)

class Answer(models.Model):
    """Answer about a specific question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    author = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'answers'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.answer}"
