from django.conf.urls import url
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup-dev/$', views.signup, name='signup-dev'),
    url(r'^signup-cli/$', views.signup, name='signup-cli'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}, name='login'),
    url(r'^profile/$', views.profile, name='profile'),

]
