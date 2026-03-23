from django.db import models

# Create your models here.
class ChaiType(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    chai_image = models.ImageField(upload_to="firstApp")
    description = models.CharField()

    def __str__(self):
        return self.name