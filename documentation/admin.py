from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'date_added')
    search_fields = ['title', 'content']

admin.site.register(Document, DocumentAdmin)
