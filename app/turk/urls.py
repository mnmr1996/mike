from django.conf.urls import url

from . import views

urlpatterns = [
    url('r^$',views.home,name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.loginform, name='login')
]
