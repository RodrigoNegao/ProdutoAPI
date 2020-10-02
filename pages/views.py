from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import (
    UpdateView,
    DeleteView
)

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
    # obj = get_object_or_404(Product, pk=pk) #.order_by('date')

    context = { 'product_form': product_form,'product_list': product_list }
    return render(request, 'base/index.html' , context) 


def product_update_view(request, pk): #pk 

    queryset = Product.objects.all()

    product = get_object_or_404(queryset, pk=pk)

     
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
    
    
    context = {'productUpdate_form': productUpdate_form,}
    return render(request, 'base/update.html',context)

    


class ProductDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

def ProductListView(request):    

    product_list = Product.objects.all() #.order_by('date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(Product, self).get_context_data(**kwargs)

        return context
        

    context = { 'product_list': product_list }

    return render(request, 'base/listProduct.html',context)

    # paginate_by = 2  # if pagination is desired