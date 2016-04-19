from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    #url(r'^bfapp/', include('bfapp.urls')),
   url(r'^admin/', include(admin.site.urls)),  #like its own app
  #  url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    #url(r'^$', views.dashboard, name='dashboard'),
     #url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
]

#url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'personal/login.html'}),   # matches /m/login

#url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),