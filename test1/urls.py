from django.conf.urls import patterns, include, url
from django.contrib import admin
#from lists import views
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','lists.views.home_page',name='home'),
    url(r'^lists/the_only_list_in_the_world/$','lists.views.view_list',name='view_list'),
    url(r'^lists/new$','lists.views.new_list',name='new_list'),
    url(r'^admin/', include(admin.site.urls)),
)
