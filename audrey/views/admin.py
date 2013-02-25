from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from audrey.models import Blog
from audrey.views import BlogAdminView

class BlogAdminIndexView(BlogAdminView,TemplateView):
    template_name = 'admin/index.html'
    
#    def get(self,request,*args,**kwargs):
#        return self.render_to_response()


class BlogAdminConfirmView(BlogAdminView,TemplateView):
    template_name = 'admin/confirm.html'
    
    def post(self,request,*args,**kwargs):
        content = request.POST.getlist("content",None)
        print request.POST
        print content 
        return self.render_to_response({'content':content})


class BlogAdminExecuteView(BlogAdminView,TemplateView):
    template_name = ''
    
    def post(self,request,*args,**kwargs):
        title = 'aaaa'
        content = request.POST.getlist("content",None)
        Blog.create(title=title,content=content)
        return HttpResponseRedirect(reverse('blog_index'))
        
