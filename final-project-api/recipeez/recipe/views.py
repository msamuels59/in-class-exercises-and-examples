from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReciperSerializer
from .models import Recipe

class RecipeView(viewsets.ModelViewSet):
    serializer_class = ReciperSerializer
    queryset = Recipe.objects.all()