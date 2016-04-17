'''
djBug Ticket Urls

Define urls for ticket application.


Created on 16 apr 2016

@author: massimo
'''

from django.conf.urls import url

from djBug.web.views import IndexView


urlpatterns = [
    url(r'^', IndexView.as_view()),
]
