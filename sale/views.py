from django.shortcuts import render

def sale(request):
    return render(request, 'sale/glav_sale.html')
