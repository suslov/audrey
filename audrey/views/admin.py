from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from audrey.models import Blog
from audrey.views import BlogAdminView,BlogContentForm

class BlogAdminIndexView(BlogAdminView,TemplateView):
    template_name = 'admin/index.html'
    
    def get(self,request,*args,**kwargs):
        form = BlogContentForm()
        return self.render_to_response({"form":form})

class BlogAdminConfirmView(BlogAdminView,TemplateView):
    template_name = 'admin/confirm.html'
    
    def post(self,request,*args,**kwargs):
        content = request.POST.getlist("content",None)
        form = BlogContentForm(request.POST)
        if not form.is_valid():
            raise
        print content
        print "a" * 19
        content = form.cleaned_data["content"]
        print content
        return self.render_to_response({'form':form})


class BlogAdminExecuteView(BlogAdminView,TemplateView):
    template_name = ''
    
    def post(self,request,*args,**kwargs):
        title = 'aaaa'
        content = request.POST.getlist("content",None)

        form = BlogContentForm(request.POST)
        print form 
        #if not form.is_valid():
        #    raise
        #form.save()
        #content = form.clean_data["content"]
        
        Blog.create(title=title,content=content)
        return HttpResponseRedirect(reverse('blog_index'))
        
