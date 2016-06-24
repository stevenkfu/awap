from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.signout),
    url(r'^manage$', views.manage),
    url(r'^about$', views.about),
    url(r'^scoreboard$', views.scoreboard),
    url(r'^admin_login$', views.admin_login),
    url(r'^admin$', views.admin),
    ]
