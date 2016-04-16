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

        # ...every ticket must have a creation datetime which must be between
        # the begin of this method and this moment
        end_time = timezone.now()
        self.assertGreaterEqual(ticket.created_on, start_time)
        self.assertLessEqual(ticket.created_on, end_time)

        # ...every ticket must have a last_update_on field with datetime of last
        # update. Creation is an update so last_update_on is between
        # the begin of this method and this moment but maybe different from created_on
        self.assertGreaterEqual(ticket.last_update_on, start_time)
        self.assertLessEqual(ticket.last_update_on, end_time)

    def test_update(self):
        """
        Test update of record for model Ticket. You can't update as you want
        last_update_on and created_on fields, but others fields can be changed.
        """
        # create a dummy ticket for testing
        ticket = Ticket.objects.create(subject="I can't create a new bug!!")

        # you can update subject
        newSubject = "I cannot create a new bug!!!"
        ticket.subject = newSubject
        ticket.save()

        self.assertEqual(ticket.subject, newSubject)
        self.fail("Incomplete Test")
