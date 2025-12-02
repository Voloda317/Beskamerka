from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from tires.models import Tire
from disks.models import Disk
from akb.models import Akb


def home(request):
    template_name = 'homepage/index.html'

    return render(request, template_name)


def search(request):
    query = request.GET.get('q', '').strip()

    tires_qs = Tire.objects.none()
    disks_qs = Disk.objects.none()
    akbs_qs = Akb.objects.none()

    if query:
        words = query.split()
        lower_words = [w.lower() for w in words]

        tire_summer = {'летняя'}

        tire_words = {'шины', 'шина', 'резина', 'колеса', 'колёса', 'летняя', 'зимняя', 'всесезонная', 'лето', 'зима', 'летние'}
        disk_words = {'диски', 'диск', 'литые', 'штампованные'}
        akb_words = {'акб', 'аккумулятор', 'аккумуляторы', 'батарея', 'батареи'}

        category = None
        if any(w in tire_words for w in lower_words):
            category = 'tires'
        elif any(w in disk_words for w in lower_words):
            category = 'disks'
        elif any(w in akb_words for w in lower_words):
            category = 'akb'

        service_words = tire_words | disk_words | akb_words
        search_words = [w for w in lower_words if w not in service_words]

        def filter_by_words(qs, fields):
            if not search_words:
                return qs
            for w in search_words:
                sub_q = Q()
                for field in fields:
                    lookup = {f'{field}__icontains': w}
                    sub_q |= Q(**lookup)
                qs = qs.filter(sub_q)
            return qs

        if category == 'tires':
            tires_qs = filter_by_words(
                Tire.objects.all(),
                ('name', 'model', 'manufacturer', 'art'),
            )
        elif category == 'disks':
            disks_qs = filter_by_words(
                Disk.objects.all(),
                ('name', 'model', 'manufacturer', 'art'),
            )
        elif category == 'akb':
            akbs_qs = filter_by_words(
                Akb.objects.all(),
                ('name', 'model', 'brand', 'art'),
            )
        else:
            tires_qs = filter_by_words(
                Tire.objects.all(),
                ('name', 'model', 'manufacturer', 'art'),
            )
            disks_qs = filter_by_words(
                Disk.objects.all(),
                ('name', 'model', 'manufacturer', 'art'),
            )
            akbs_qs = filter_by_words(
                Akb.objects.all(),
                ('name', 'model', 'brand', 'art'),
            )

    # ---- пагинация ----
    def make_page(qs, per_page, param_name):
        paginator = Paginator(qs, per_page)
        page_number = request.GET.get(param_name)
        return paginator.get_page(page_number)

    tires = make_page(tires_qs, 12, 'page_tires')
    disks = make_page(disks_qs, 12, 'page_disks')
    akbs = make_page(akbs_qs, 12, 'page_akbs')

    context = {
        'query': query,
        'tires': tires,
        'disks': disks,
        'akbs': akbs,
    }
    return render(request, 'search/search_results.html', context)
