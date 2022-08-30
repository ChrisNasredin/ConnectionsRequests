from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=50,
                            blank=True,
                            null=True,
                            verbose_name='ФИО')
    address = models.CharField(max_length=60,
                               blank=True,
                               null=True,
                               verbose_name='Адрес'
                               )
    phone = models.CharField(max_length=12,
                             blank=True,
                             null=True,
                             verbose_name='Телефон'
                             )
    state = models.ForeignKey('State',
                              null=True,
                              default=1,
                              on_delete=models.PROTECT,
                              verbose_name='Статус')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class State(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Статус')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
