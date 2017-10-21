from django.conf.urls import url
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}, name='login'),
    url(r'^profile/$', views.profile, name='profile'),

]
