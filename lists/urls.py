from django.conf.urls import patterns, include, url
#from lists import views
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lists/(\d+)/$','lists.views.view_list',name='view_list'),
    url(r'^lists/(\d+)/add_item$','lists.views.add_item',name='add_item'),
    url(r'^lists/new$','lists.views.new_list',name='new_list'),
)