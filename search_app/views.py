from django.shortcuts import render
from app_1.models import Product
from django.db.models import Q

# Create your views here.

def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        print('Query Value:', query)
        products=Product.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))
        print('Product Value:',products)
    return render(request, 'search_app.html', {'query':query, 'products':products})
