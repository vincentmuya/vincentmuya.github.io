from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url, include
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='index'),
    url(r'^skills/$',views.skills,name='skills'),
    url(r'^projects/$',views.projects,name='projects'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^auto-reply/$',views.auto_reply,name='auto_reply'),
    ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
