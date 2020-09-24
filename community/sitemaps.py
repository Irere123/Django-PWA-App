# This helps my site to be seen by a Search Engine like Google or Bing


from django.contrib.sitemaps import Sitemap # Importing sitemap from the sitemaps framework
from .models import Question # Import The Question Model

class PostSitemap(Sitemap):
 changefreq = 'monthly'
 priority = 0.9

 def items(self):
   return Question.objects.all()
   
 def lastmod(self, obj):
   return obj.pub_date