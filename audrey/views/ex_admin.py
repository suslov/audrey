from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from audrey.models import Blog
from audrey.views import BlogAdminView,BlogContentForm

class BlogAdminIndexView(BlogAdminView,TemplateView):
    template_name = 'ex_admin/index.html'
    
    def get(self,request,*args,**kwargs):
        form = BlogContentForm()
        return self.render_to_response({"form":form})

class BlogAdminConfirmView(BlogAdminView,TemplateView):
    template_name = 'ex_admin/confirm.html'
    
    def post(self,request,*args,**kwargs):
        
        form = BlogContentForm(request.POST)

        if not form.is_valid():
            raise

        return self.render_to_response({'form':form})


class BlogAdminExecuteView(BlogAdminView,TemplateView):
    template_name = ''
    
    def post(self,request,*args,**kwargs):
        form = BlogContentForm(request.POST)

        if not form.is_valid():
            raise

        obj = form.save(commit=False)
        obj.created_at,obj.updated_at = [datetime.now()] * 2
        obj.save()

        return HttpResponseRedirect(reverse('blog_index'))
        
