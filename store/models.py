
from django.db import models
from django.contrib.auth.models import  User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True);
    phone = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name

class Brand(models.Model):
    brandName = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.brandName

class Product(models.Model):
    brand = models.ForeignKey(Brand,on_delete = models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    quantitySelled = models.IntegerField(default=0)
    dateAdded =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True)

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.SET_NULL,null=True,blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,blank=False)
    shippedDate =  models.DateTimeField()



    def get_number_item(self):
        orderitem = self.orderitem_set.all()
        sum = 0;
        for item in orderitem:
            sum+= item.quatity;
        return sum;
    def get_total_price_item(self):
        orderItem = self.orderitem_set.all()
        sum = 0
        for item in orderItem:
            sum+=item.total_price()
        return sum

class Orderdetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=0,null=True,blank=True)
    description = models.TextField(null=True, blank=True)

    def total_price(self):
        return self.product.price*self.quatity
class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    def __init__(self):
        return self.categoryName


class Category_Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)

class Cart(models.Model):
    dateAdded = models.DateField(auto_now_add=True)
    quantity = models.IntegerField();

class Cart_Product(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)