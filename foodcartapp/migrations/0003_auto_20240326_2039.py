# Generated by Django 3.2.15 on 2024-03-26 20:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0002_auto_20240326_2026"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "заказ", "verbose_name_plural": "заказы"},
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.TextField(default=True, verbose_name="адрес доставки"),
        ),
        migrations.AlterField(
            model_name="order",
            name="comment",
            field=models.TextField(blank=True, verbose_name="комментарий к заказу"),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="дата создания"),
        ),
        migrations.AlterField(
            model_name="order",
            name="firstname",
            field=models.CharField(max_length=40, verbose_name="имя"),
        ),
        migrations.AlterField(
            model_name="order",
            name="lastname",
            field=models.CharField(max_length=40, verbose_name="фамилия"),
        ),
        migrations.AlterField(
            model_name="order",
            name="phonenumber",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "Необработанный"),
                    ("cooking", "Готовится"),
                    ("delivery", "Доставляется"),
                    ("closed", "Завершен"),
                ],
                db_index=True,
                default="new",
                max_length=15,
                verbose_name="статус",
            ),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="contact_phone",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="контактный телефон"
            ),
        ),
    ]
