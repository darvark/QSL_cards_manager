from django.db import models

# Create your models here.
class KartaQSL(models.Model):
    znak = models.CharField(max_length=20)
    qso_data = models.DateField()
    wyslana = models.BooleanField(default=True)
    odebrana = models.BooleanField(default=False)

    def __str__(self):
        return self.znak

