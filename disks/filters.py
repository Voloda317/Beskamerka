import django_filters
from django import forms
from .models import Disk

class DiskFilter(django_filters.FilterSet):
    WHEEL_TYPE_CHOICES = [
        ('Литой', 'Литой'),
        ('Штампованные', 'Штампованный'),
    ]
    
    disk_type = django_filters.MultipleChoiceFilter(
        choices=WHEEL_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Тип диска'
    )

    width = django_filters.MultipleChoiceFilter(
        field_name='width',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Ширина'
    )

    diameter = django_filters.MultipleChoiceFilter(
        field_name='diameter',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Диаметр'
    )

    bolts = django_filters.MultipleChoiceFilter(
        field_name='bolts',
        choices=[], 
        widget=forms.CheckboxSelectMultiple,
        label='Кол-во отверстий'
    )

    pcd = django_filters.MultipleChoiceFilter(
        field_name='pcd',
        choices=[], 
        widget=forms.CheckboxSelectMultiple,
        label='PCD (межболтовое расстояние)'
    )

    dia_min = django_filters.NumberFilter(
        field_name='dia',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'от'}),
        label='DIA от'
    )

    dia_max = django_filters.NumberFilter(
        field_name='dia', 
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'до'}),
        label='DIA до'
    )

    et_min = django_filters.NumberFilter(
        field_name='et',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'от'}),
        label='ET от'
    )   

    et_max = django_filters.NumberFilter(
        field_name='et',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'до'}),
        label='ET до'
    )

    brand = django_filters.MultipleChoiceFilter(
        field_name='manufacturer',
        choices=[], 
        widget=forms.CheckboxSelectMultiple,
        label='Бренд'
    )

    model = django_filters.MultipleChoiceFilter(
        field_name='model',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Модель'
    )

    price_min = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'от'}),
        label='Цена от'
    )

    price_max = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'до'}),
        label='Цена до'
    )

    in_stock = django_filters.BooleanFilter(
        field_name='quantity',
        lookup_expr='gt',
        widget=forms.CheckboxInput,
        label='Только в наличии'
    )

    class Meta:
        model = Disk
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.filters['width'].extra['choices'] = [
            (width, width) for width in Disk.objects.values_list('width', flat=True).distinct().order_by('width')
        ]
        self.filters['diameter'].extra['choices'] = [
            (diameter, diameter) for diameter in Disk.objects.values_list('diameter', flat=True).distinct().order_by('diameter')
        ]
        self.filters['bolts'].extra['choices'] = [
            (bolts, bolts) for bolts in Disk.objects.values_list('bolts', flat=True).distinct().order_by('bolts')
        ]
        self.filters['pcd'].extra['choices'] = [
            (pcd, pcd) for pcd in Disk.objects.values_list('pcd', flat=True).distinct().order_by('pcd')
        ]
        self.filters['brand'].extra['choices'] = [
            (manufacturer, manufacturer) for manufacturer in Disk.objects.values_list('manufacturer', flat=True).distinct().order_by('manufacturer')
        ]
        self.filters['model'].extra['choices'] = [
            (model, model) for model in Disk.objects.values_list('model', flat=True).distinct().order_by('model')
        ]