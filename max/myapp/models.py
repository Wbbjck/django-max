from django.db import models

# Create your models here.
class Protocols(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    number = models.PositiveIntegerField(
        default=1,
        null=True,
        verbose_name="Номер протокола",
    )
    date = models.DateField(
        verbose_name="Дата"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Адрес дома"
    )
    file = models.FileField(
        upload_to='protocols/%Y/'
    )

    class Meta:
        verbose_name_plural = "Протоколы"


    def __str__(self):
        return str(self.number) + ' - ' + str(self.date)

class ReestrTSZH(models.Model):
    id = models.AutoField(
        primary_key=True
    )
   
    name = models.CharField(
        max_length=150,
        verbose_name="Фамилия"
        )
    surname = models.CharField(
        max_length=150,
        verbose_name="Имя"
        )
    otchestvo = models.CharField(
        max_length=150,
        verbose_name="Отчество"   
    )
    
    date = models.DateField(
        verbose_name="Дата вступления"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Адрес"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Номер паспорта"
    )

    class Meta:
        verbose_name_plural = "Реестр ТСЖ"


    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.otchestvo)

class Scans(models.Model):
        member = models.ForeignKey(ReestrTSZH, on_delete=models.CASCADE)
        file = models.FileField(
            upload_to='statements/%Y/'
        )
    