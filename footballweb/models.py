from django.db import models
from .managers import FootballManager

from django.db.models.query import QuerySet



class Kraj():
        NIEZNANY = 6
        HISZPANIA = 0
        ANGLIA = 1
        WŁOCHY = 2
        NIEMCY = 3
        FRANCJA = 4
        POLSKA = 5
        KRAJE = (
            (HISZPANIA, 'Hiszpania'),
            (ANGLIA, 'Anglia'),
            (WŁOCHY, 'Włochy'),
            (NIEMCY, 'Niemcy'),
            (FRANCJA, 'Francja'),
            (POLSKA, 'Polska'),
            (NIEZNANY, 'Nieznany')
        )




class Football(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=1900) 
    opis = models.TextField(default="")
    lig_mistrzów = models.PositiveSmallIntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to="logosy", null=True, blank=True)
    kraj = models.PositiveSmallIntegerField(default=6, choices=Kraj.KRAJE)

    objects = models.Manager()
    kraje = FootballManager()


    def __str__(self):
        return self.tytul_z_rokiem()
    
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)





