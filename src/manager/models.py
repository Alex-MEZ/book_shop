from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'
    title = models.CharField(max_length=100,verbose_name='название книги')
