from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    #localhost/index
    url(r'^$', views.index, name = 'index'),
    url(r'^person/([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_person/$', views.post_person, name = 'post_person'),
    url(r'^user/(\w+)/$', views.profile, name = 'profile'),
    url(r'^user_login/$', views.user_login, name = 'user_login'),
    url(r'^user_logout/$', views.user_logout, name = 'user_logout'),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, { 'document_root' : settings.MEDIA_ROOT, }),
    ]
