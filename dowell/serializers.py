from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Population

class PopulationFunctionSerializer(ModelSerializer):
    class Meta:
        model = Population
        fields = '__all__'
