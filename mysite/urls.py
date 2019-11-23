from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import include
admin.autodiscover()
from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
  	url(r'^admin/',include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^password/$',core_views.change_password, name='change_password'),
    #url('^change_password/$', auth_views.password_change, {'post_change_redirect': 'next_page'}, name='password_change'),
    url(r'^edit_profile/$',core_views.edit_profile, name='edit_profile'),
    url(r'^export_view/$',core_views.export_view, name='export_view'),
    url(r'^Add_form/$',core_views.Add_form, name='Add_form'),
    url(r'^view_responses/$',core_views.view_responses, name='view_responses'),
]
