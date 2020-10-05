from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField(blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
