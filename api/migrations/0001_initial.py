# Generated by Django 4.2.7 on 2023-11-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Letter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fio_sender",
                    models.CharField(max_length=150, verbose_name="ФИО отправителя"),
                ),
                (
                    "fio_recipient",
                    models.CharField(max_length=150, verbose_name="ФИО получателя"),
                ),
                (
                    "sending_point",
                    models.CharField(max_length=150, verbose_name="пункт отправки"),
                ),
                (
                    "receiving_point",
                    models.CharField(max_length=150, verbose_name="пункт получения"),
                ),
                (
                    "index_place_dispatch",
                    models.PositiveBigIntegerField(
                        verbose_name="индекс места отправки"
                    ),
                ),
                (
                    "index_place_receipt",
                    models.PositiveBigIntegerField(
                        verbose_name="индекс места получения"
                    ),
                ),
                (
                    "type_letter",
                    models.SmallIntegerField(
                        choices=[
                            (0, "Письмо"),
                            (1, "заказное письмо"),
                            (2, "ценное письмо"),
                            (3, "экспресс-письмо"),
                        ],
                        verbose_name="тип письма",
                    ),
                ),
                (
                    "letter_weight",
                    models.PositiveBigIntegerField(verbose_name="вес письма"),
                ),
            ],
            options={
                "verbose_name": "Письмо",
                "verbose_name_plural": "Письма",
            },
        ),
        migrations.CreateModel(
            name="Package",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fio_sender",
                    models.CharField(max_length=150, verbose_name="ФИО отправителя"),
                ),
                (
                    "fio_recipient",
                    models.CharField(max_length=150, verbose_name="ФИО получателя"),
                ),
                (
                    "sending_point",
                    models.CharField(max_length=150, verbose_name="пункт отправки"),
                ),
                (
                    "receiving_point",
                    models.CharField(max_length=150, verbose_name="пункт получения"),
                ),
                (
                    "index_place_dispatch",
                    models.PositiveBigIntegerField(
                        verbose_name="индекс места отправки"
                    ),
                ),
                (
                    "index_place_receipt",
                    models.PositiveBigIntegerField(
                        verbose_name="индекс места получения"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=50, verbose_name="телефон для извещения"
                    ),
                ),
                (
                    "type_package",
                    models.SmallIntegerField(
                        choices=[
                            (0, "мелкий пакет"),
                            (1, "посылка"),
                            (2, "посылка 1 класса"),
                            (3, "ценная посылка"),
                            (4, "посылка международная"),
                            (5, "экспресс-посылка"),
                        ],
                        verbose_name="тип посылки",
                    ),
                ),
                (
                    "payment_amount",
                    models.PositiveBigIntegerField(verbose_name="сумма платежа"),
                ),
            ],
            options={
                "verbose_name": "Посылка",
                "verbose_name_plural": "Посылки",
            },
        ),
    ]
