from django.db import models
#somewaht like a database
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length =50000)
    
