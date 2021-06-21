from rest_framework import serializers
from .models import animal
class animalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = animal
        fields = ('name', 'age' , 'specie' , 'weight' , 'blood_type')