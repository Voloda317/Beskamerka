from django.views.generic import ListView
from .filters import AkbFilter
from .models import Akb

class AkbListView(ListView):
    model = Akb
    template_name = 'akb/akb.html'   # убедись, что шаблон лежит по этому пути
    context_object_name = 'akbs'

    def get_queryset(self):
        qs = super().get_queryset().order_by('brand', 'model')
        self.filterset = AkbFilter(self.request.GET, queryset=qs)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['request'] = self.request
        return context
