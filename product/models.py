from django.db import models
from PIL import Image
from category.models import Category


# def upload_location1 (filename):
#     return "products/P-%s/%s" %(filename)

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=60)    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pictureProduct = models.ImageField( upload_to='products/', #TODO pic with name/P-{0}/{0}' .format(productName), #upload_location1, #'products/P-%s/%s' %(productName),
                                        default='default/default1.png')
    description = models.TextField(max_length=120)
    categories = models.ManyToManyField(Category,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.productName

    #Resize Image Install Pillow
    def save(self,**kwargs):
        super().save()
        img1 = Image.open(self.pictureProduct.path)

        if img1.height > 300 or img1.width > 300:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.pictureProduct.path)