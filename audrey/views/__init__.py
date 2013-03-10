from django.forms import ModelForm
from django.views.generic.base import View

from audrey.models import Blog,Comment

class BlogBaseView(View):
    pass


class BlogView(BlogBaseView):
    pass


class BlogAdminView(BlogBaseView):
    pass

class BlogContentForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('created_at','updated_at',)

class BlogContentForm(ModelForm):
    class Meta:
        model = Comment

