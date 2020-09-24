from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Models 

# This is for the timestamp that defines when a question has been added
# It will return a string like:
    # '2 days ago', '20 seconds ago' and so on...
def x_ago_helper(diff):
    if diff.days > 0:
        return f'{diff.days} days ago'
    if diff.seconds < 60:
        return f'{diff.seconds} seconds ago'
    if diff.seconds < 3600:
        return f'{diff.seconds // 60} minutes ago'
    return f'{diff.seconds // 3600} hours ago'


class Topic(models.Model):
    """ A topic the user is learning about."""
    text = models.CharField(max_length= 200)
    overview = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    @property
    def num_entries(self):
        entries = Entry.objects.filter(topic_id = self.id)
        return len(entries)

    def x_ago(self):
        diff = timezone.now() - self.date_added
        return x_ago_helper(diff)

class Entry(models.Model):
    """Something specific about a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}....."
