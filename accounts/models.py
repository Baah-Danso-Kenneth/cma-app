from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        indexes = [models.Index(fields=['-date_created'])]

    def __str__(self):
        return self.name


class Product(models.Model):
    class Category(models.TextChoices):
        IN_DOOR='IN DOOR'
        OUT_DOOR='OUT DOOR'
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.CharField(max_length=15, choices=Category.choices, default=Category.IN_DOOR)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'OUT DOOR'
        DELIVERED = 'DELIVERED'
        OUT_OF_STOCK = 'OUT OF STOCK'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_customer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.PENDING)
