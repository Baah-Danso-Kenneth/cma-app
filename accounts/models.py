from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=13, null=True)
    email=models.EmailField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        indexes=[models.Index(fields=['-date_created'])]

    def __str__(self):
        return self.name
