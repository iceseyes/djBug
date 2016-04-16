"""
Models for djBug Ticket App
============================

Those models describe a bug notification and its history.
"""

from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    """
    Define a ticket object.

    A ticket object is a bug notification/improve request. When user sees something
    that he doesn't like in a project, he *open* a new ticket.
    """
    STATE_TO_APPROVE = "to_approve"
    STATE_APPROVED = "approved"
    STATE_CLOSED = "closed"
    STATE_NOTABUG = "not_a_bug"
    STATE_WONTFIX = "wontfix"
    STATES = (
        (STATE_TO_APPROVE, "To Approve"),
        (STATE_APPROVED, "Approved"),
        (STATE_CLOSED, "Closed"),
        (STATE_NOTABUG, "Not a Bug"),
        (STATE_WONTFIX, "Won't fix"),
    )

    subject = models.CharField(max_length=40, null=False, blank=False, default=None)
    description = models.TextField()
    state = models.CharField(max_length=10, choices=STATES, default=STATE_TO_APPROVE)
    created_on = models.DateTimeField(default=timezone.now)
    last_update_on = models.DateTimeField(default=timezone.now)
