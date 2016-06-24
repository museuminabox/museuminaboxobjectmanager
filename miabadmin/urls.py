from apps.home.views import Home
from apps.organisations.views import (
    OrganisationList,
    OrganisationCreate,
    OrganisationDetail,
)

from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^organisations/?$',
        OrganisationList.as_view(),
        name='organisation-list',
    ),
    url(
        r'^organisations/new/?$',
        OrganisationCreate.as_view(),
        name='organisation-create',
    ),
    url(
        r'^organisations/(?P<pk>\d+)/?$',
        OrganisationDetail.as_view(),
        name='organisation-detail',
    ),
]
