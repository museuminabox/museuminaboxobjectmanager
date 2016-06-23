from apps.home.views import Home
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
