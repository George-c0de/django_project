from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    fio_sender = models.CharField("ФИО отправителя", max_length=150)
    fio_recipient = models.CharField("ФИО получателя", max_length=150)
    sending_point = models.CharField("пункт отправки", max_length=150)
    receiving_point = models.CharField("пункт получения", max_length=150)
    index_place_dispatch = models.PositiveBigIntegerField("индекс места отправки")
    index_place_receipt = models.PositiveBigIntegerField("индекс места получения")


class Letter(BaseModel):
    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    class LetterTypeChoices(models.IntegerChoices):
        LETTER = 0, _("Письмо")
        REGISTERED_LETTER = 1, _("заказное письмо")
        VALUABLE_LETTER = 2, _("ценное письмо")
        EXPRESS_LETTER = 3, _("экспресс-письмо")

    type_letter = models.SmallIntegerField("тип письма", choices=LetterTypeChoices.choices)
    letter_weight = models.PositiveBigIntegerField("вес письма")


class Package(BaseModel):
    class Meta:
        verbose_name = "Посылка"
        verbose_name_plural = "Посылки"

    class LetterTypeChoices(models.IntegerChoices):
        SMALL_PACKAGE = 0, _("мелкий пакет")
        PACKAGE = 1, _("посылка")
        CLASS_FIRST_PACKAGE = 2, _("посылка 1 класса")
        VALUABLE_PACKAGE = 3, _("ценная посылка")
        PACKAGE_INTERNATIONAL = 4, _("посылка международная")
        EXPRESS_PACKAGE = 5, _("экспресс-посылка")

    phone = models.CharField("телефон для извещения", max_length=50)
    type_package = models.SmallIntegerField("тип посылки", choices=LetterTypeChoices.choices)
    payment_amount = models.PositiveBigIntegerField("сумма платежа")
