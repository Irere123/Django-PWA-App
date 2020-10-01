from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=500)
    cover_image = models.ImageField(upload_to='media', blank=True)
    video = models.FileField(upload_to='media', blank=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
