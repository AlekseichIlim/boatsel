from django.db import models

class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='лодка')

    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(max_length=100, verbose_name='почта')
    message = models.TextField(verbose_name='сообщение')

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True)
#     для сущностей генерируемых пользователями, автоматически заполняется текущая дата и время

    def __str__(self):
        return f'Заказ на лодку {self.boat.name} от {self.name}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

