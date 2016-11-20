from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    #localhost/index
    url(r'^$', views.index, name = 'index'),
    url(r'^person/([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_person/$', views.post_person, name = 'post_person'),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, { 'document_root' : settings.MEDIA_ROOT, }),
    ]
