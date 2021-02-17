from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата")

class Meta:
    verbose_name_plural = "Объявления"
    verbose_name = "Объявление"
    ordering = ['-date']
