# Generated by Django 3.2.15 on 2024-03-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0004_auto_20240328_0929"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "Наличные"), ("card", "Электронный платеж")],
                db_index=True,
                default="cash",
                max_length=15,
                verbose_name="способ оплаты",
            ),
        ),
    ]