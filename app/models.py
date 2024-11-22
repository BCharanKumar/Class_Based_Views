from django.db import models

# Create your models here.

class Category(models.Model):
    product_category=models.CharField(max_length=25)
    def __str__(self):
        return self.product_category
    
class Product(models.Model):
    pname=models.CharField(max_length=50)
    pid=models.IntegerField(primary_key=True)
    price=models.IntegerField()
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.pname
    

class School(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sadd=models.TextField()
    def __str__(self):
        return self.sname