import markdown
from django.views.generic.base import TemplateView

from audrey.models import Blog

from audrey.views import BlogView

class BlogIndexView(BlogView,TemplateView):

    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        blogs = Blog.get_newest() 
        return self.render_to_response({'blogs':blogs})


class BlogDetailView(BlogView,TemplateView):

    template_name = 'detail.html'

    def get(self,request,*args,**kwargs):
        blog_id = int(kwargs.get('blog_id',None))
        if blog_id is None:
            pass
        blog = Blog.get_or_none(blog_id)
        return self.render_to_response({'blog':blog})

class BlogArchiveView(BlogView,TemplateView):

    template_name = 'archive.html'

    def get(self,request,*args,**kwargs):
        return self.render_to_response({'hello':'hello'})
    

class BlogSearchView(BlogView,TemplateView):

    template_name = 'search.html'

    def get(self,request,*args,**kwargs):
        words = request.Get.getlist('words',None)
        if words is None:
            pass
        words_list = words.split()
        return self.render_to_response({'hello':'hello'})
    

class BlogCommentView(BlogView,TemplateView):

    def post(self,request,*args,**kwargs):
        return self.render_to_response({'hello':'hello'})

