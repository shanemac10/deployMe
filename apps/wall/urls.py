from django.conf.urls import url
from . import views
#SECRESTS.APPS.WALL.URLS
#namespace = wall
urlpatterns = [
    url(r'^secrets$', views.secrets, name='secrets'),
    url(r'^supersecrets$', views.supersecrets, name='supersecrets'),
    url(r'^tell$', views.tell, name='tell'),
    url(r'^like/(?P<secret_id>\d+)$', views.like, name='like'),
    url(r'^delete/(?P<secret_id>\d+)$', views.delete, name='delete'),

]
