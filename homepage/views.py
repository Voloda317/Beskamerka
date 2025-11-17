from django.shortcuts import render
from django.db.models import Q

from tires.models import Tire
from disks.models import Disk
from akb.models import Akb


def home(request):
    template_name = 'homepage/index.html'

    title = 'Привет'
    carrot = 'заяц!'

    context = {
        'title': title,
        'carrot': carrot,
    }

    return render(request, template_name, context)


def search(request):
    query = request.GET.get('q', '').strip()

    tires = disks = akbs = []

    if query:
        tires = Tire.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(art__icontains=query)
        )

        disks = Disk.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(manufacturer__icontains=query) |
            Q(art__icontains=query)
        )

        akbs = Akb.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(brand__icontains=query) |
            Q(art__icontains=query)
        )

    context = {
        'query': query,
        'tires': tires,
        'disks': disks,
        'akbs': akbs,
    }
    return render(request, 'search/search_results.html', context)
