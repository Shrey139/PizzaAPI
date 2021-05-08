from rest_framework import viewsets
from .models import Pizza
from .serializers import PizzaSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()