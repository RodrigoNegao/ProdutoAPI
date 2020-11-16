from django.test import TestCase
from product.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(productName="Joao", price="1")
        print ("okss")
        # Product.objects.create(name="cat", sound="meow")

    # def test_product(self):
    #     """test product"""
    #     lion = Product.objects.get(name="lion")
    #     cat = Product.objects.get(name="cat")
    #     # self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     # self.assertEqual(cat.speak(), 'The cat says "meow"')

