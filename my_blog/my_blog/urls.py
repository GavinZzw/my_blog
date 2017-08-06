"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views
from article.views import RSSFeed

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = 'home'),
    url(r'^article/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^time/(?P<t_time>\d+)/$', views.search_time, name='search_time'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
    url(r'^search/$',views.blog_search, name = 'search'),
    # url(r'^ckeditor/', include('ckeditor.urls')),
]
