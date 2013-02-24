from django.views.generic.base import TemplateView

from audrey.views import BlogAdminView

class BlogAdminView(BlogAdminView,TemplateView):
    template_name = 'admin/admin.html'
    
    def get(self,request,*args,**kwargs):
        return self.render_to_response()


class BlogAdminConfirmView(BlogAdminView,TemplateView):
    template_name = 'admin/admin_confirm.html'
    
    def get(self,request,*args,**kwargs):
        return self.render_to_response()


class BlogAdminExecuteView(BlogAdminView,TemplateView):
    template_name = ''
    
    def get(self,request,*args,**kwargs):
        return self.render_to_response()
