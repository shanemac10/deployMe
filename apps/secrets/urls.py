from django.conf.urls import url
from . import views
#APPS.SECRETS>URLS
#namespace=secrets
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
# url(r'^(?P<number>\d+)$', views.show, name='show')
]
