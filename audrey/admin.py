from django.contrib import admin
from audrey.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fields = ['title','content']

admin.site.register(Blog,BlogAdmin)

