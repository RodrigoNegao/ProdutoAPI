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
        #salva os dados e a foto
        product_form = ProductForm(data=request.POST,files=request.FILES,)
        # Verifica se o formulario é valido
        if product_form.is_valid(): 
            # Salva o produto
            product_form.save()
            # Confirma com mensagem na tela
            messages.success(request, 'Produto Salvo com Sucesso')
            #Vai para pagina principal
            return HttpResponseRedirect(reverse('index'))
        else:
            # Avisa o motivo do erro no shell.
            print(product_form.errors)

    else:
        # Renderiza um formulario para cadastro .
        product_form = ProductForm()

    # Cria uma lista por ordem decrescente por data
    product_list = Product.objects.all().order_by('-date') 
 
    #Paginação
    page_number = request.GET.get('page') 
    paginator = Paginator(product_list,3) # Mostra nemero de itens por pagina, no caso 3.
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.get_page(page_number)
    

    context = { 'product_form': product_form, 'pages':pages }
    return render(request, 'base/index.html' , context) 

def filter_view(request):
    #Faz um GET da informação de pesquisa
    search_query = request.GET.get('search_box')
    # | == OR Faz a filtro de acordo que foi digitado
    productfilter = (Q(productName__icontains=search_query) 
                    | Q(description__icontains=search_query) ) 
    product_list = Product.objects.filter(productfilter).order_by('-date')

    #Paginação
    page_number = request.GET.get('page')
    paginator = Paginator(product_list,3) # Mostra nemero de itens por pagina, no caso 3.
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.get_page(page_number)

    context = { 'pages':pages }
    return render(request, 'base/search.html' , context)



def product_update_view(request, pk):
    #lista todos os produtos
    product_list = Product.objects.all()
    #filtra o produto de acordo a pk da pagina
    product_choice = Product.objects.filter(pk=pk)

    #filtra o produto de acordo a pk da pagina para usar a pk correspondente com o produto
    product = get_object_or_404(product_list, pk=pk)
     
    if request.method == 'POST':
        #salva o formulurio e a foto
        product_update_form = ProductForm(data=request.POST,files=request.FILES,instance=product)
        
        if product_update_form.is_valid(): 
            # Salva o produto
            product_update_form.save()

            messages.success(request, 'Produto Modificado com Sucesso')
   
            return HttpResponseRedirect(reverse('index'))
        else:
            
            print(product_update_form.errors)

    else:
        # renderiza o formulario com dados que estao no banco de dados
        product_update_form = ProductForm(instance=product)

    
    context = {'product_update_form': product_update_form, 'product_choice':product_choice ,'product_list': product_list}
    return render(request, 'base/update.html',context)

    


def product_delete_view(request,pk):

    product_choice = Product.objects.filter(pk=pk)

    context ={'product_choice':product_choice} 
  
    # filtra a pk do link com a pk do banco de dados  
    obj = get_object_or_404(Product, pk = pk)   
  
    if request.method =="POST": 
        # deleta a o item/produto que tem a pk em comum
        obj.delete() 
        # Confirma o comando
        messages.success(request, 'Produto Apagado com Sucesso')
        #vai para a pagina principal
        return HttpResponseRedirect(reverse('index')) 
  
    return render(request, "base/delete.html", context) 
