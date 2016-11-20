from django.conf.urls import url
from . import views

urlpatterns = [
    #localhost/index
    url(r'^$', views.index, name = 'index'),
    url(r'^person/([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_person/$', views.post_person, name = 'post_person'),
]
