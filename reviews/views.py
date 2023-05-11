from django.shortcuts import render
from .serializers import ReviewSerializer
from .models import Reviews
from users.permissions import IsUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ReviewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsUser | IsAuthenticated]

