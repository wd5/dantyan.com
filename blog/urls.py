#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
#from models import Post


#(?P<year>\d{4})
urlpatterns = patterns('blog',
    url(r'^$', 'views.home', name='blog-home' ),
    url(r'^category-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.category', name='blog-category'),
    url(r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.post', name='blog-post'),
    url(r'^add', 'views.add', name='blog-add'),
    url(r'^edit/(?P<id>\d+)', 'views.edit', name='blog-edit'),
    #url(r'^cat', 'views.cat', name='blog-cat'),
)

