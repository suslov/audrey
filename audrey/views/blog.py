
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from audrey.models import Blog,Comment

from audrey.views import BlogView,BlogContentForm

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
        blog.count += 1
        blog.save()

        comments = Comment.get_from_blog(blog)
        form = BlogContentForm()

        relevant_blogs = blog.get_relevant()
        recent_blogs = None
        if not relevant_blogs:
            recent_blogs = blog.get_newest()

        return self.render_to_response({'blog':blog,
                                        'comments':comments,
                                        'form':form,
                                        'relevant_blogs':relevant_blogs,
                                        'recent_blogs':recent_blogs})

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
        print 'aaaaaaa'
        print kwargs
        blog_id = int(kwargs.get('blog_id'),0)
        #reply_to = int(kwargs.get('reply_to'),0)
        if blog_id is None:
            pass

        form = BlogContentForm(request.POST)
        if not form.is_valid():
           return HttpResponseRedirect(reverse('blog_index'))

        obj = form.save(commit=False)
        #if reply_to:
        #    obj.reply_to = reply_to
        obj.blog = Blog.objects.get(id=blog_id)
        obj.save()

        return HttpResponseRedirect(reverse('blog_detail',args=[blog_id]))

