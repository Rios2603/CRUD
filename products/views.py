from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm
from django.contrib import messages

# Create your views here.
def Index(request):
  return render(request, 'products/index.html')

def LogIn(request):
  return render(request, 'products/login.html')

def CreateProduct(request):
  if request.method == 'POST':
    form = ProductsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('productos')
  else:
    form = ProductsForm()
  context = {'form' : form}
  return render(request, 'products/agregar.html', context)

def ReadProduct(request):
  products = Products.objects.all()
  context = {'products' : products}
  return render(request, 'products/productos.html', context)

def UpdateProduct(request, cod_product):
  product = Products.objects.get(cod_product = cod_product)
  if request.method == 'POST':
    form = ProductsForm(request.POST, instance= product)
    if form.is_valid():
      form.save()
      messages.success(request, "Modificado Correctamente")
      return redirect('productos')
  else:
    form = ProductsForm(instance= product)
  context = {'form' : form}
  return render(request, 'products/editar.html', context)

def DeleteProduct(request, cod_product):
  product = Products.objects.get(cod_product = cod_product)
  product.delete()
  return redirect('productos')