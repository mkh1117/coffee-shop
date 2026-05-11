from django.shortcuts import render
from product.models import Product
from cart.models import Cart


def home(request):
    products1 = Product.objects.all()
    products2 = Product.objects.order_by('?')

    context = {'products1': products1, 'products2': products2}
    return render(request, 'index.html', context)
