from django.db import models

class Base(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='base/',
        verbose_name='Логотип'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Главная'