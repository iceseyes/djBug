'''
djBug Ticket Urls

Define urls for ticket application.


Created on 16 apr 2016

@author: massimo
'''

from django.conf.urls import url, include
from rest_framework import routers
from djBug.ticket import views


router = routers.DefaultRouter()
router.register(r'tickets', views.TicketViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
