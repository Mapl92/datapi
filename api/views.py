from rest_framework import viewsets
from rest_framework import generics
from .serializers import GemeindenSerializer
from .models import Gemeinden
from django.db.models.functions import Length


class GemeindenViewSet(viewsets.ModelViewSet):
    queryset = Gemeinden.objects.all().order_by('gemeinde')
    serializer_class = GemeindenSerializer
    filter_fields = ('gemeinde')

class TaxList(generics.ListAPIView):
    serializer_class = GemeindenSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        filter_fields = ('category', 'in_stock')
        gemeinde = self.kwargs['gemeinde']
        
        return Gemeinden.objects.filter(gemeinde__startswith=gemeinde).order_by(Length('gemeinde'))[:5]

