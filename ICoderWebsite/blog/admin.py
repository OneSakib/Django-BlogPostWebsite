from django.contrib import admin
from .models import Blog, BlogComment

# Register your models here.
admin.site.register(BlogComment)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)
