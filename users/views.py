from django.shortcuts import render
from rest_framework import viewsets,status
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUser,ReadOnly

# Create your views here.
User = get_user_model()

class UserViewSet(viewsets.ViewSet):

    def list(self,request):
        users = User.objects.all()
        serializer = CustomUserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = CustomUserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = CustomUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,repuest,pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    def partial_update(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.action == 'list':
            permissions_classes = [IsAuthenticated]
        else:
            permissions_classes = [IsUser,ReadOnly]

        return [permission for permission in permissions_classes]



