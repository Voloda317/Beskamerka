from django.db import models

class Disk(models.Model):
    art = models.CharField(verbose_name='артикул', max_length=70, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='полное название')
    quantity = models.IntegerField(verbose_name='Колличество')
    price = models.IntegerField(verbose_name='Цена')
    disk_type = models.CharField(max_length=100, verbose_name='Тип диска') 
    manufacturer = models.CharField(max_length=100, verbose_name='брэнд')
    model = models.CharField(max_length=255, verbose_name='модель', null=True, blank=True)
    width = models.FloatField(verbose_name='Ширина диска(B)')
    diameter = models.FloatField(verbose_name='Диаметр диска(D)')
    bolts = models.IntegerField(verbose_name='Кол-во отверстий')
    et = models.FloatField(verbose_name='Вылет(et,мм)')
    pcd = models.FloatField(verbose_name='PCD(межболтовое расст)')
    dia = models.FloatField(verbose_name='Центральное отверстие(DIA, мм)')
    color = models.CharField(max_length=100, verbose_name='цвет')
    img = models.URLField(verbose_name='ссылка на фото', null=True, blank=True)

    class Meta:
        verbose_name = 'диск'
        verbose_name_plural = 'диски' 

    def __str__(self):
        return self.name
