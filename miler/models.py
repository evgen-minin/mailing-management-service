from django.db import models
from django.conf import settings


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Mailing(models.Model):
    STATUS_CHOICES = (
        ("created", "Создана"),
        ("started", "Запущена"),
        ("completed", "Завершена"),
    )

    FREQUENCY_CHOICES = (
        ("daily", "Раз в день"),
        ("weekly", "Раз в неделю"),
        ("monthly", "Раз в месяц"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mailings"
    )
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="mailings"
    )
    send_time = models.TimeField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")

    def __str__(self):
        return f"Рассылка ID: {self.pk}"

    class Meta:
        verbose_name_plural = "Почтовое отправление"


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Сообщение"


class DeliveryAttempt(models.Model):
    STATUS_CHOICES = (
        ("success", "Успешно"),
        ("failed", "Неудачно"),
    )

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.status} ({self.timestamp})"

    class Meta:
        verbose_name_plural = "Попытка доставки"
