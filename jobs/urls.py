from django.conf.urls import *
from . import views
from django.contrib import admin
from .views import IndexView

urlpatterns = [
    #url(r'^bfapp/', include('bfapp.urls')),
   url(r'^admin/', include(admin.site.urls)),  #like its own app
   
    url(r'^$', IndexView.as_view(), name='index'),
    #url(r'^seekoremp/$', views.seekoremp, name='seekoremp'),
    #url(r'^dashboard/', include('jobs.urls')),
    url(r'^employerbase/$', views.employerbase, name='employerbase'),
    url(r'^employerdash/$', views.employerdash, name='employerdash'),
    url(r'^employerfaq/$', views.employerfaq, name='employerfaq'),
    url(r'^employerservice/$', views.employerservice, name='employerservice'),
    url(r'^employeraccount/$', views.employeraccount, name='employeraccount'),
    url(r'^employerabout/$', views.employerabout, name='employerabout'),
    #url(r'^employerdash/', include('jobs.urls')),
    # url(r'^employerfaq/', include('jobs.urls')),
    # url(r'^employerbase/', include('jobs.urls')),
   # url(r'^dashboard/', include('jobs.urls')),
   url(r'^seekerbase/$', views.seekerbase, name='seekerbase'),
   url(r'^seekerdash/$', views.seekerdash, name='seekerdash'),
    url(r'^seekerfaq/$', views.seekerfaq, name='seekerfaq'),
    url(r'^seekerservice/$', views.seekerservice, name='seekerservice'),
    url(r'^seekeraccount/$', views.seekeraccount, name='seekeraccount'),
    url(r'^seekeredu/$', views.seekeredu, name='seekeredu'),
    url(r'^seekerupload/$', views.seekerupload, name='seekerupload'),
    url(r'^seekerabout/$', views.seekerabout, name='seekerabout'),
    
    url(r'^search/$', views.search, name='search'),
    
    url(r'^name/$', views.get_name, name='name'),
    url(r'^seekerreg/$', views.seekerreg, name='seekerreg'),
    #url(r'^contact/', views.contact, name='contact'),
    #url(r'^$', views.home, name='home'),
     #url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
]

#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'personal/login.html'}),   # matches /m/login

#url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),