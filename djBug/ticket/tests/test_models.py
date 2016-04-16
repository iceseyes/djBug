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

from djBug.ticket.models import Ticket


class TicketTestCase(TestCase):
    """
    Test Case for Ticket Model
    """

    def test_create(self):
        """
        Test creation of a new ticket
        """

        # create a new empty ticket fails cause at least a subject must be provided.
        with transaction.atomic():
            self.assertRaises(IntegrityError, Ticket.objects.create)

        # therefore create a new empty ticket with subject.
        ticket = Ticket.objects.create(subject="I can't create a new bug!!")

        # ...an empty ticket has no description
        self.assertEqual(ticket.description, "")

        self.fail("Incomplete Test")
