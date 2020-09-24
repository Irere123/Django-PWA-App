from django.contrib import admin
from .models import Topic, Entry

#Customizing The admin page
admin.site.site_header = 'Learn Scholar Adminstration' # The <h1>Learn Scholar Adminstration</h1>
admin.site.site_title = 'Learn Scholar Admin Area' # The ??????????
admin.site.index_title= 'Welcome to Learn Scholar Admin Area' # The <title>Welcome to Learn Scholar Admin Area</title>

# Registering my models
admin.site.register(Topic) # This registers the Topic model
admin.site.register(Entry) # This registers the Entry model