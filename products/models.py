from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=233)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=233)
    price = models.FloatField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],blank=True,null=True)
    image = models.ImageField(upload_to='products')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_price(self):
        if not self.discount:
            return self.price
        else:
            return (self.price*(100-self.discount))

class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ordered'
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_total_item(self):
        return self.product.get_price()*self.quantity

