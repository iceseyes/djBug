'''
djBug Ticket serializers
========================

Serializers are classes used by external programs (like js Ui).


Created on 16 apr 2016

@author: massimo
'''
from rest_framework import serializers

from djBug.ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    """
    Manage serialization for `djBug.ticket.models.Ticket`
    """

    class Meta:
        model = Ticket
        fields = ("id", "subject", "description", "state", "created_on", "last_update_on")
