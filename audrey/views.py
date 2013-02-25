from django.views.generic.base import TemplateView

from audrey.
class BlogIndexView(TemplateView):

    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        return self.render_to_response({'hello':'hello'})

class BlogDetailView
