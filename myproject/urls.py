from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.list import ListView
from myblog.models import Tag, MyBlog
from django.views.generic.detail import DetailView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls), name='admin-site'),
    url(r'^$', ListView.as_view(model = MyBlog, template_name = 'myblog/blog_list.html'), name='blog_list'),
    url(r'^details/(?P<pk>[0-9]+)/', DetailView.as_view(model = MyBlog, template_name ='myblog/blog_details.html'), name = 'blog_details'),
)
