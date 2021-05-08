from .models import Pizza, TOPPING
from rest_framework import serializers, fields

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
    topping = serializers.MultipleChoiceField(choices=TOPPING)
