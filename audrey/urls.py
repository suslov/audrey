from django.conf.urls import patterns,url
from audrey.views.blog import (BlogIndexView,
                               BlogDetailView,
                               BlogCommentView,
                               BlogArchiveView,
                               BlogSearchView)

from audrey.views.ex_admin import (BlogAdminIndexView,
                               BlogAdminConfirmView,
                               BlogAdminExecuteView)

urlpatterns = patterns('audrey.views',
    url(r'^$',BlogIndexView.as_view(),name='blog_index'),
    url(r'^detail/(?P<blog_id>\d+)/$',BlogDetailView.as_view(),name='blog_detail'),
    url(r'^comment/(?P<blog_id>\d+)/$',BlogCommentView.as_view(),name='blog_comment'),
    url(r'^archive/$',BlogArchiveView.as_view(),name='blog_archive'),
    url(r'^search/$',BlogSearchView.as_view(),name='blog_search'),

    url(r'^ex_admin/$',BlogAdminIndexView.as_view(),name='blog_admin'),
    url(r'^ex_admin/confirm/$',BlogAdminConfirmView.as_view(),name='blog_admin_confirm'),
    url(r'^ex_admin/execute/$',BlogAdminExecuteView.as_view(),name='blog_admin_execute'),
)
