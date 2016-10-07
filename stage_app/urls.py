"""stage_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from stage.views import index, events, concerts, theatre, circus, EventDetail, search, contact
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^events/$', events, name='events'),
    url(r'^events/concerts/$', concerts, name='concerts'),
    url(r'^events/theatre/$', theatre, name='theatre'),
    url(r'^events/circus/$', circus, name='circus'),
    url(r'^events/(?P<event_artist_name>.+)/info/$', EventDetail.as_view(), name='info'),
    url(r'^search/$', search, name='search'),
    url(r'^contact/$', contact, name='contact'),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
# serve files from media folder
        urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
                        ]
