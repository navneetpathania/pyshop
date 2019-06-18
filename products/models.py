from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    stock = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
