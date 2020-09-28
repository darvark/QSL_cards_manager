from django.db import models

class Operator(models.Model):
    operator = models.CharField(max_length=20)

    def __str__(self):
        return self.operator

# Create your models here.
class KartaQSL(models.Model):
    znak = models.CharField(max_length=20)
    qso_data = models.DateField()
    wyslana = models.BooleanField(default=True)
    odebrana = models.BooleanField(default=False)
    operator = models.ForeignKey("karty.Operator", on_delete=models.CASCADE)

    def __str__(self):
        return self.znak

