from django.db import models


class Product(models.Model):
    name = models.CharField(max_length= 100)
    image = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length= 100)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.name} - {self.price}"