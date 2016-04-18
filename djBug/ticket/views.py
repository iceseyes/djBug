from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from djBug.ticket.models import Ticket
from djBug.ticket.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """

    queryset = Ticket.objects.all().order_by('-last_update_on')
    serializer_class = TicketSerializer
    permission_classes = (AllowAny, )
    ordering_fields = ('-last_update_on')
