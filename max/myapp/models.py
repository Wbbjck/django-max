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

