# Generated by Django 3.2.15 on 2024-03-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0006_auto_20240329_1132"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="called_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="дата звонка"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivered_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="дата доставки"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("cash", "Наличными (при получении)"),
                    ("card", "Картой (при оформлении)"),
                ],
                db_index=True,
                default="cash",
                max_length=15,
                verbose_name="способ оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="registered_at",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="дата создания"
            ),
        ),
    ]