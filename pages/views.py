from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from product.models import Product
from pages.forms import CreateProductForm


# Create your views here.
def index(request):
    if request.method == 'POST':

        product_form = CreateProductForm(data=request.POST,files=request.FILES,)
        # Check to see the form is valid
        if product_form.is_valid(): # and profile_default.is_valid() :
            # Sava o produto
            product_form.save()
            # Registration Successful! messages.success
            messages.success(request, 'Produto Salvo com Sucesso')
            #Go to Index
            return HttpResponseRedirect(reverse('index'))
        else:
            # One of the forms was invalid if this else gets called.
            print(product_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        product_form = CreateProductForm()

    product_list = Product.objects.all() #.order_by('date')

    context = { 'product_form': product_form,'product_list': product_list }
    return render(request, 'base/index.html' , context) 


def ProductListView(request):
    

    product_list = Product.objects.all() #.order_by('date')

    context = { 'product_list': product_list }

    return render(request, 'base/listProduct.html',context)

    # paginate_by = 2  # if pagination is desired