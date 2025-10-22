from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Tire
from .filters import TireFilter

class TireListView(ListView):
    model = Tire
    template_name = 'tires/tires.html'
    context_object_name = 'tires'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TireFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

def tire_detail(request, tire_id):
    tire = get_object_or_404(Tire, id=tire_id)
    context = {
        'tire': tire,
    }
    return render(request, 'tires/tire_detail.html', context)