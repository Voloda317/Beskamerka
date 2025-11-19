from django.shortcuts import render

def services_list(request): 
    return render(request, 'services/services.html')

def tire_services(request):
    return render(request, 'services/tire_services.html')

def balancing(request):
    return render(request, 'services/balancing.html')

def pravka(request):
    return render(request, 'services/pravka.html')

def remont(request):
    return render(request, 'services/remont_tires.html')

def keeping_tires(request):
    return render(request, 'services/keeping_tires.html')