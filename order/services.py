from django.conf import settings
from django.core.mail import send_mail

from boat.models import Boat

from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        'Заявка на покупку лодки',
        f'{order_item.name} ({order_item.email}) хочет купить вашу лодку {order_item.boat.name}. Сообщение: {order_item.message}',
        'Alekseich-ilim@yandex.ru',
        [order_item.boat.owner.email],
    )
    # settings.EMAIL_HOST_USER - это настройка в settings.py вашего проекта