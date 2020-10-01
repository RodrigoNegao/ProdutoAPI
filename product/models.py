from django.db import models
from PIL import Image
from category.models import Category


# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=60,verbose_name="Nome do Produto")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Preço")
    pictureProduct = models.ImageField( upload_to='products/', #TODO pic with name
                                        default='default/default1.png',verbose_name="Imagem")
    description = models.TextField(max_length=120,verbose_name="Descrição")
    categories = models.ForeignKey(Category,blank=True,null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.productName
    
    # def upload_location1 (productName):
    #     return "accounts/avatars/%s/%s" %(productName)

    #Resize Image Install Pillow
    def save(self,**kwargs):
        super().save()
        img1 = Image.open(self.pictureProduct.path)

        if img1.height > 300 or img1.width > 300:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.pictureProduct.path)