from datetime import datetime
from django.db import models
from django.db.models import F

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category')

    @classmethod
    def create(cls,title=title,content=content):
        return cls.objects.create(title=title,content=content,
                                    created_at = datetime.now())

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
    def get_newest(cls,num=5,exclude=None):
        if exclude is None:
            return cls.objects.all().order_by('-updated_at')[:num]

    @classmethod
    def get_most_read(cls,num=5):
        return cls.objects.all().order_by('-count')[:num]

    def get_relevant(self,num=5):
        category = self.category.all()
        cls = self.__class__
        return cls.objects.filter(category__in=category).exclude(id=self.id)[:num]

    @property
    def next(self):
        cls = self.__class__
        try:
            return cls.objects.get(id=self.id+1)
        except cls.DoesNotExist:
            return cls.objects.get(id=1)

    @property
    def previous(self):
        cls = self.__class__
        try:
            return cls.objects.get(id=self.id-1)
        except cls.DoesNotExist:
            return cls.objects.all().order_by('-id')[0]

    def __unicode__(self):
        return self.title
        

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category_name


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    comment = models.TextField()
    reply_to = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_from_blog(cls,blog):
        return cls.objects.filter(blog=blog)

    def __unicode__(self):
        return '{}:{}'.format(self.blog.title,self.comment[:50])

