from django.db import models

# Create your models here.
class Akb(models.Model):
    art = models.CharField('артикул', max_length=32)
    brand = models.CharField('бренд', max_length=50)
    model = models.CharField('модель', max_length=50)
    name = models.CharField('полное название', max_length=150)
    count = models.IntegerField('количество')
    price = models.IntegerField('цена')
    length = models.IntegerField('длина')
    width = models.IntegerField('ширина')
    height = models.IntegerField('высота')
    container = models.IntegerField('емкость')
    start_current = models.IntegerField('пусковой ток')
    polarity = models.CharField('полярность', max_length=10)
    weight = models.CharField("вес", max_length=50)
    image_url = models.URLField('ссылка на фото', blank=True, null=True)

    class Meta: 
        verbose_name = 'аккумулятор'
        verbose_name_plural = 'аккумуляторы'    
    
    def __str__(self):
        return self.name
    