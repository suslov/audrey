from datetime import datetime
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    @classmethod
    def create(cls,title=title,content=content):
        return cls.objects.create(title=title,content=content,
                           created_at = datetime.now(),
                           updated_at = datetime.now())

    @classmethod
    def get_or_none(cls,id):
        try:
            return cls.objects.get(id=id)
        except cls.DataDoesNotExist:
            return None

    @classmethod
    def get_or_create(cls,id=id,title=None,content=None):
        blog = cls.get_or_none(id=id)
        if blog is None:
            blog = cls.create(id=id,content=content)
        return blog

    @classmethod
    def get_newest(cls,num=5):
        return cls.objects.all().order_by('-updated_at')[0:num]
        
