'''
DjBug Ticket Models test unit
===============================

Part of djBug project.

Created on 16 apr 2016

@author: massimo bianchi
'''
from django.test.testcases import TestCase

from django.db import transaction
from django.db.utils import IntegrityError

from django.utils import timezone

from djBug.ticket.models import Ticket


class TicketTestCase(TestCase):
    """
    Test Case for Ticket Model
    """

    def test_create(self):
        """
        Test creation of a new ticket
        """

        start_time = timezone.now()

        # create a new empty ticket fails cause at least a subject must be provided.
        with transaction.atomic():
            self.assertRaises(IntegrityError, Ticket.objects.create)

        # therefore create a new empty ticket with subject.
        ticket = Ticket.objects.create(subject="I can't create a new bug!!")

        # ...an empty ticket has no description
        self.assertEqual(ticket.description, "")

        # ...default state is TO_APPROVE
        self.assertEqual(ticket.state, Ticket.STATE_TO_APPROVE)

        # ...every tickect must have a creation datetime which must be between
        # the begin of this method and this moment
        end_time = timezone.now()
        self.assertGreaterEqual(ticket.created_on, start_time)
        self.assertLessEqual(ticket.created_on, end_time)

        self.fail("Incomplete Test")
