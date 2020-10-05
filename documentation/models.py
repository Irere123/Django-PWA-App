from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=500)
    cover_image = models.ImageField(upload_to='images')
    date_added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
