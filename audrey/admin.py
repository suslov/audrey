from django.contrib import admin
from audrey.models import Blog,Category

class BlogAdmin(admin.ModelAdmin):
    #fields = ['title','content']
    pass

admin.site.register(Blog,BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)

#TODO for debug
from audrey.models import Comment

class CommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment,CommentsAdmin)