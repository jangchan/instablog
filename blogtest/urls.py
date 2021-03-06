from django.conf.urls import include, url

from django.contrib.auth.views import login as login
from django.contrib.auth.views import logout as logout

from . import views

urlpatterns = [
    url(r'^posts/$', views.list_posts, name='list_posts'),
    url(r'^posts/create/$', views.create_post, name='create_post'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.view_post, name='view_post'),
    url(r'^posts/(?P<pk>[0-9]+)/delete/$', views.delete_post, name='delete_post'),

    # url(r'^login/$', login, {'template_name':'login.html'}, name='login'), 
    # url(r'^logout/$', logout, {'next_page':'/login/'}, name='logout'),
]
