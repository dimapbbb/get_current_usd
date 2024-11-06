from locale import currency

from django.db import models


class CurrencyRequest(models.Model):
    currency_choices = [
        ('USD', 'Американкий доллар'),
    ]
    currency = models.CharField(choices=currency_choices, verbose_name='Валюта')
    value = models.CharField(verbose_name='Полученное значение в рублях')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время запроса')

    def __str__(self):
        return f"{str(self.created_at)[:19]} : 1 {self.currency} = {self.value} рублей"

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

