from rest_framework.serializers import ModelSerializer
from .models import Reviews
from products.serializers import CustomUserSerializer,ProductSerializer

class ReviewSerializer(ModelSerializer):
    user = CustomUserSerializer()
    product = ProductSerializer()
    class Meta:
        model = Reviews
        fields = '__all__'