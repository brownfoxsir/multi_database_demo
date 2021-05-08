from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = verbose_name = 'books'

    def __str__(self):
        return self.name