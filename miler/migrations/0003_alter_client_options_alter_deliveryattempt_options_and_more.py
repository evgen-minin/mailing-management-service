# Generated by Django 4.2.4 on 2023-08-20 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miler', '0002_blogarticle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='deliveryattempt',
            options={'verbose_name_plural': 'Попытка доставки'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name_plural': 'Почтовое отправление'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'Сообщение'},
        ),
    ]