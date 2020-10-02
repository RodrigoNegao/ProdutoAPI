from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)

from product.models import Product
from pages.forms import ProductForm



# Create your views here.
def index(request):
    if request.method == 'POST':

        product_form = ProductForm(data=request.POST,files=request.FILES,)
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
        product_form = ProductForm()


    product_list = Product.objects.all()
    #Paginator
    page_number = request.GET.get('page') #, 1
    paginator = Paginator(product_list,3) # Show 6 contacts per page.
    pages = paginator.get_page(page_number) 
    # try:
    #     pages = paginator.page(page)
    # except PageNotAnInteger:
    #     pages = paginator.page(1)
    # except EmptyPage:
    #     pages = paginator.page(paginator.num_pages)

    context = { 'product_form': product_form,'product_list': product_list, 'pages':pages }
    return render(request, 'base/index.html' , context) 


def product_update_view(request, pk): #pk 

    product_list = Product.objects.all()

    product = get_object_or_404(product_list, pk=pk)

     
    if request.method == 'POST':

        productUpdate_form = ProductForm(data=request.POST,files=request.FILES,instance=product)
        # Check to see the form is valid
        if productUpdate_form.is_valid(): # and profile_default.is_valid() :
            # Sava o produto
            productUpdate_form.save()
            # Registration Successful! messages.success
            messages.success(request, 'Produto Modificado com Sucesso')
            #Go to Index
            return HttpResponseRedirect(reverse('index'))
        else:
            # One of the forms was invalid if this else gets called.
            print(productUpdate_form.errors)

    else:
        # render the forms with data.
        productUpdate_form = ProductForm(instance=product)    
    
    context = {'productUpdate_form': productUpdate_form, 'product_list': product_list}
    return render(request, 'base/update.html',context)

    


def product_delete_view(request,pk):
    # dictionary for initial data with  
    # field names as keys
    product_list = Product.objects.all()

    context ={'product_list':product_list} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Product, pk = pk)   
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # Registration Successful! messages.success
        messages.success(request, 'Produto Apagado com Sucesso')
        #Go to Index
        return HttpResponseRedirect(reverse('index')) 
  
    return render(request, "base/delete.html", context) 


    # paginate_by = 2  # if pagination is desired