from django.contrib import admin
from .models import BlogPost
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.
class BlogAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["post_title", "post_published"]}),
        ("URL", {'fields': ["post_slug"]}),
        ("Content", {'fields': ["post_content"]})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
        
admin.site.register(BlogPost, BlogAdmin)