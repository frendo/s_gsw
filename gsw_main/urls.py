from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gsw_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('apps.home_g.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^polls/', include('apps.polls.urls', namespace="polls")),
]
