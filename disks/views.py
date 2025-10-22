from django.shortcuts import render
from .models import Disk
from django.views.generic import ListView
from .filters import DiskFilter

class DiskListView(ListView):
    model = Disk 
    template_name = 'disks/disks.html'
    context_object_name = 'disks'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DiskFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context