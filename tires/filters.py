import django_filters
from django import forms
from .models import Tire

class TireFilter(django_filters.FilterSet):
    width = django_filters.MultipleChoiceFilter(
        field_name='width',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Ширина'
    )
    
    height = django_filters.MultipleChoiceFilter(
        field_name='height',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Высота'
    )
    
    radius = django_filters.MultipleChoiceFilter(
        field_name='radius',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Радиус'
    )

    SEASON_CHOICES = [
        ('Лето', 'Лето'), 
        ('Зима', 'Зима'), 
    ]

    season = django_filters.MultipleChoiceFilter(
        field_name='season',
        choices=SEASON_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Сезон'
    )

    THORNS_CHOICES = [
        
    ]

    brand = django_filters.MultipleChoiceFilter(
        
    )


    brand = django_filters.MultipleChoiceFilter(
        field_name='manufacturer',
        choices=[], 
        widget =forms.CheckboxSelectMultiple,
        label='Бренд'
    )

    model = django_filters.MultipleChoiceFilter(
        field_name = 'model',
        choices = [],
        widget = forms.CheckboxSelectMultiple,
        label = 'Модель'
    )

    
    class Meta:
        model = Tire
        fields = ['width', 'height', 'radius', 'season', 'brand', 'model']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['width'].extra['choices'] = [
            (width, width) for width in Tire.objects.values_list('width', flat=True).distinct().order_by('width')
        ]
        self.filters['height'].extra['choices'] = [
            (height, height) for height in Tire.objects.values_list('height', flat=True).distinct().order_by('height')
        ]
        self.filters['radius'].extra['choices'] = [
            (radius, radius) for radius in Tire.objects.values_list('radius', flat=True).distinct().order_by('radius')
        ]
        self.filters['brand'].extra['choices'] = [
            (brand, brand) for brand in Tire.objects.values_list('manufacturer', flat=True).distinct().order_by('manufacturer')
        ]
        self.filters['model'].extra['choices'] = [
            (model, model) for model in Tire.objects.values_list('model', flat=True).distinct().order_by('model')
        ]
