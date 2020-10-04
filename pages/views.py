from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)

from product.models import Product
from pages.forms import ProductForm
#filters
from django.db.models import Q



# Create your views here.
def index(request):
    if request.method == 'POST':

        product_form = ProductForm(data=request.POST,files=request.FILES,)
        # Check to see the form is valid
        if product_form.is_valid(): 
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
        # Was not an HTTP post so we just render the forms .
        product_form = ProductForm()


    product_list = Product.objects.all().order_by('-date') 
 
    #Paginator #TODO number of pages
    page_number = request.GET.get('page') #, 1
    paginator = Paginator(product_list,3) # Show 6 contacts per page.
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.get_page(page_number)
    
    print (product_list)
    print (pages)

    context = { 'product_form': product_form, 'pages':pages }
    return render(request, 'base/index.html' , context) 

def filter_view(request):
    search_query = request.GET.get('search_box')
    # | == OR
    productfilter = (Q(productName__icontains=search_query) 
                    | Q(description__icontains=search_query) ) #| Q(price=search_query)#TODO   DECIMAL Q(categories_id=search_query)) 
    product_list = Product.objects.filter(productfilter).order_by('-date')

    #Paginator
    page_number = request.GET.get('page')
    paginator = Paginator(product_list,3) # Show 6 contacts per page.
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.get_page(page_number)

    context = { 'pages':pages }
    return render(request, 'base/search.html' , context)



def product_update_view(request, pk): #pk 

    product_list = Product.objects.all()

    product_choice = Product.objects.filter(pk=pk)

    product = get_object_or_404(product_list, pk=pk)
     
    if request.method == 'POST':

        product_update_form = ProductForm(data=request.POST,files=request.FILES,instance=product)
        # Check to see the form is valid
        if product_update_form.is_valid(): # and profile_default.is_valid() :
            # Sava o produto
            product_update_form.save()
            # Registration Successful! messages.success
            messages.success(request, 'Produto Modificado com Sucesso')
            #Go to Index
            return HttpResponseRedirect(reverse('index'))
        else:
            # One of the forms was invalid if this else gets called.
            print(product_update_form.errors)

    else:
        # render the forms with data.
        product_update_form = ProductForm(instance=product)

        print(product_update_form)
    
    context = {'product_update_form': product_update_form, 'product_choice':product_choice ,'product_list': product_list}
    return render(request, 'base/update.html',context)

    


def product_delete_view(request,pk):
    # dictionary for initial data with  
    # field names as keys
    product_choice = Product.objects.filter(pk=pk)

    context ={'product_choice':product_choice} 
  
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
