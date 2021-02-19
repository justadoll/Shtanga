from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата")
    rubric = models.ForeignKey('Rubric',null=True,on_delete=models.PROTECT, verbose_name="Рубрика")

class Meta:
    verbose_name_plural = "Объявления"
    verbose_name = "Объявление"
    ordering = ['-date']

class Rubric(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20, db_index=True, verbose_name="Haзвaниe")

class Meta:
    verbose_name_plural = "Рубрики"
    verbose_name = "Рубрика"
    ordering = ['name']
