from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser

# Create your models here
class Reviews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description} -> {self.rating} by {self.user.username}'
    class Meta:
        ordering = ('-created_at', '-rating')
