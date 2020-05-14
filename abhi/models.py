from django.db import models

# Create your models here.
class data(models.Model):
    information =models.TextField(max_length=200,blank=False,null=False)
    itemMark=models.BooleanField(default=False)
    account_id=models.IntegerField()



    
    