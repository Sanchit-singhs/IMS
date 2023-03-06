from django.conf import settings
from django.db import models
# Create your models here.

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    quantity_in_stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name
