import django_filters
from django import forms
from .models import Akb

class AkbFilter(django_filters.FilterSet):
    brand = django_filters.MultipleChoiceFilter(
        field_name='brand',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Брэнд'
    )

    model = django_filters.MultipleChoiceFilter(
        field_name='model',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Модель',
    )

    min_container = django_filters.NumberFilter(
        field_name='container',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'от'}),
        label='Емкость от'
    )

    max_container = django_filters.NumberFilter(
        field_name='container',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'до'}),
        label='Емкость до'
    )

    min_start_current = django_filters.NumberFilter(
        field_name='start_current',
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'от'}),
        label='Пусковой ток от'
    )

    max_start_current = django_filters.NumberFilter(
        field_name='start_current',
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'до'}),
        label='Пусковой ток до'
    )

    polarity = django_filters.MultipleChoiceFilter(
        field_name='polarity',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Полярность',
    )

    width = django_filters.MultipleChoiceFilter(
        field_name='width',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Ширина',
    )

    height = django_filters.MultipleChoiceFilter(
        field_name='height',
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Высота'
    )

    class Meta:
        model = Akb
        fields = ['brand', 'model', 'polarity', 'width', 'height', 'weight']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['brand'].extra['choices'] = [
            (b, b) for b in Akb.objects.values_list('brand', flat=True).distinct().order_by('brand')
        ]
        self.filters['model'].extra['choices'] = [
            (m, m) for m in Akb.objects.values_list('model', flat=True).distinct().order_by('model')
        ]
        self.filters['polarity'].extra['choices'] = [
            (p, p) for p in Akb.objects.values_list('polarity', flat=True).distinct().order_by('polarity')
        ]
        self.filters['width'].extra['choices'] = [
            (w, w) for w in Akb.objects.values_list('width', flat=True).distinct().order_by('width')
        ]
        self.filters['height'].extra['choices'] = [
            (h, h) for h in Akb.objects.values_list('height', flat=True).distinct().order_by('height')
        ]
