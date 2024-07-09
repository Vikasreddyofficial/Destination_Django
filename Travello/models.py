from django.db import models

# Create your models here.
# class Destination: this is not a model ,-> this is simple class
#     name:str
#     desc:str
#     price:int
#     img:str
#     offer:bool

class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

