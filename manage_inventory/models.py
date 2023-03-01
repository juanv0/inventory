from django.db import models

# Create your models here.
class Moto(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    model_up = models.IntegerField()
    model_down = models.IntegerField() 

    def __str__(self):
        return "%s %s" %(self.brand,self.name)

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    price = models.IntegerField()
    models = models.ForeignKey(Moto, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.code, self.name, self.price)
