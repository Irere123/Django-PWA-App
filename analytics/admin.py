from django.contrib import admin
from .models import ObjectViewed

class ObjectViewedAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content_type','object_id','timestamp', 'user')
    search_fields = ['content_type', 'user']


# Register your models here.
admin.site.register(ObjectViewed, ObjectViewedAdmin)
