from django.shortcuts import render
from rest_framework import viewsets
from .serializers import animalSerializer
from .models import animal

# Create your views here.

class AnimalView(viewsets.ModelViewSet):
    queryset = animal.objects.all()
    serializer_class = animalSerializer
