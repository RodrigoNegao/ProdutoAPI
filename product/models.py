from django.db import models
from PIL import Image
from django.urls import reverse
from category.models import Category
from django.template.defaultfilters import slugify


# Create your models here.

class Product(models.Model):
    pk_id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=60,verbose_name="Nome do Produto")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Preço")
    pictureProduct = models.ImageField( upload_to='products/', #TODO save pic with name
                                        default='default/default1.png',verbose_name="Imagem")
    description = models.TextField(max_length=120,verbose_name="Descrição")
    categories = models.ForeignKey(Category,blank=True,null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(editable=False, auto_now=True)
    # slug = models.SlugField(default='',editable=False, max_length=30, null = False)

    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk }) #{% url 'post-detail' post.pk %}
    
    # def upload_location1 (productName):
    #     return "accounts/avatars/%s/%s" %(productName)

    #Resize Image Install Pillow
    def save(self,**kwargs):
        # value = self.productName
        # self.slug = slugify(value, allow_unicode=True)
        # super().save(*args, **kwargs)
        super().save()
        img1 = Image.open(self.pictureProduct.path)

        if img1.height > 300 or img1.width > 300:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.pictureProduct.path)