# (c) Crown Owned Copyright, 2016. Dstl.

from django.http import HttpResponse
from django.views.generic.base import View


class Home(View):

    #   Get the homepage.
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
