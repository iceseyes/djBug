"""
Models for djBug Ticket App
============================

Those models describe a bug notification and its history.
"""

from django.db import models


class Ticket(models.Model):
    """
    Define a ticket object.

    A ticket object is a bug notification/improve request. When user sees something
    that he doesn't like in a project, he *open* a new ticket.
    """
    subject = models.CharField(max_length=40, null=False, blank=False, default=None)
    description = models.TextField()
