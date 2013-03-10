from datetime import datetime
from django.db import models
from django.db.models import F

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category')
    comments = models.OneToOneField('Comment',null=True, blank=True, default = None)

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
            return cls.objects.all().order_by('-updated_at')[0:num]

    def get_relevant(self,num=5):
        category = self.category.all()
        cls = self.__class__
        return cls.objects.filter(category__in=category).exclude(id=self.id)[0:num]

    def __unicode__(self):
        return self.title
        

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.category_name


class Comment(models.Model):
    author = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    reply_to = models.IntegerField(null=True)
    #created_at = models.DateTimeField(default=None,auto_now=True)

    def __unicode__(self):
        pass



class Guzai(models.Model):

    guzai = models.CharField(max_length=200)
    def __unicode__(self):
        return self.guzai
    class Meta:
        ordering = ('guzai',)

class Gohan(models.Model):

    gohan = models.CharField(max_length=200)
    guzais = models.ManyToManyField(Guzai)

    def __unicode__(self):
        return self.gohan
    class Meta:
        ordering = ('gohan',)
