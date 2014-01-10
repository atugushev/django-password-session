try:
    from django.conf.urls import url, patterns, include
except ImportError:  # for Django 1.3 compatibility
    from django.conf.urls.defaults import url, patterns, include

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)