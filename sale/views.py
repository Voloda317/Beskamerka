from django.shortcuts import render

def sale_tire_list(request):
    context = {
        'sale': 'your_sale_data_here',  # Добавьте ваши данные
    }
    return render(request, 'sale/glav_sale.html', context)