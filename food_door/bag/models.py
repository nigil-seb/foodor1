from django.db import models
from foodoorapp.models import Item
# Create your models here.
class Bag(models.Model):
    bag_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Bag'
        ordering=['date_added']
    def __str__(self):
        return self.bag_id
class BagItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    bag=models.ForeignKey(Bag,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='BagItem'

    def sub_total(self):
        return self.item.price*self.quantity
    def __str__(self):
        return self.item