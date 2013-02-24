from django.conf.urls import patterns,url
from audrey.views.blog import (BlogIndexView,
                               BlogDetailView,
                               BlogArchiveView,
                               BlogSearchView)

from audrey.views.blog import (BlogAdminView,
                               BlogAdminConfirmView,
                               BlogAdminExecuteView)

urlpatterns = patterns('audrey.views',
    url(r'^index/$',BlogIndexView.as_view(),name='blog_index'),
    url(r'^detail/(?P<blog_id>\d+)/$',BlogDetailView.as_view(),name='blog_detail'),
    url(r'^archive/$',BlogArchiveView.as_view(),name='blog_archive'),
    url(r'^search/$',BlogSearchView.as_view(),name='blog_search'),

    url(r'^ex_admin/$',BlogAdminView.as_view(),name='blog_admin'),
    url(r'^ex_admin/confirm$',BlogAdminView.as_view(),name='blog_admin_confirm'),
    url(r'^ex_admin/execute/$',BlogAdminExecuteView.as_view(),name='blog_admin_execute')
)
