from django.db import models

from products.models import Order

# Create your models here.
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    PAYMENT_CHOICES = (
        ('CASH', 'CASH'),
        ('CARD', 'CARD'),
    )
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='CASH')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'payment for {self.order.user.username}'