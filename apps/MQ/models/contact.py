from django.db import models

class Contact(models.Model):
    name = models.CharField(
        max_length=155
    )
    email = models.EmailField()
    subject = models.CharField(
        max_length=155
    )
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Контакты'