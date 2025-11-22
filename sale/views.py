from django.shortcuts import render

def sale(request):
    return render(request, 'sale/glav_sale.html')

def seasonal_storage(request):
    return render(request, 'sale/seasonal_storage.html')

def free_tire_service(request):
    return render(request, 'sale/free_tire_service.html')

def free_shippping(request):
    return render(request, 'sale/free_shipping.html')

def sale_doship(request):
    return render(request, 'sale/sale_doship.html')
