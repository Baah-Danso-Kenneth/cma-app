from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    profile_pic=models.ImageField(default='mood.png',null=True,blank=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        indexes = [models.Index(fields=['-date_created'])]

    def __str__(self):
        return self.name or self.email or str(self.id) or self.user


class Tags(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Category(models.TextChoices):
        IN_DOOR = 'IN DOOR'
        OUT_DOOR = 'OUT DOOR'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=15, choices=Category.choices, default=Category.IN_DOOR)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tags)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        DELIVERED = 'DELIVERED'
        OUT_OF_STOCK = 'OUT OF STOCK'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f" {self.product.name}"
