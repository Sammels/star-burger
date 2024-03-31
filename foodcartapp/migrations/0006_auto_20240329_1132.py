# Generated by Django 3.2.15 on 2024-03-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0005_order_payment_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="restaurant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                to="foodcartapp.restaurant",
                verbose_name="Исполнитель",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "Необработанный"),
                    ("COOKING", "Готовится"),
                    ("DELIVERY", "Доставляется"),
                    ("CLOSED", "Завершен"),
                ],
                db_index=True,
                default="NEW",
                max_length=15,
                verbose_name="статус",
            ),
        ),
    ]