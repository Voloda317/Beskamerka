from django.db import models

class Tire(models.Model):
    art = models.CharField('артикул', max_length=32, null=True)
    name = models.CharField('полное название', max_length=150)
    quantity = models.IntegerField('количество')
    price = models.IntegerField('цена')
    manufacturer = models.CharField('бренд', max_length=50)
    model = models.CharField('модель', max_length=50)
    season = models.CharField('сезон', max_length=10)  # лето/зима
    width = models.IntegerField('ширина')
    height = models.IntegerField('высота')
    radius = models.IntegerField('радиус')
    speed_index = models.CharField('индекс скорости', max_length=50)  # напр. "T (190 км/ч)"
    load_index = models.CharField('индекс нагрузки', max_length=50)    # напр. "95 (690 кг)"
    thorns = models.BooleanField('шипы', default=False)
    image_url = models.URLField('ссылка на фото', blank=True, null=True)

    class Meta:
        verbose_name = 'шина'
        verbose_name_plural = 'шины'

    def __str__(self):
        return self.name
