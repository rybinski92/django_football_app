from django.db import models
# from .models import Kraj


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

class FootballQuerySet(models.QuerySet):

    def poland_only(self):
        return self.filter(kraj=Kraj.POLSKA)    
    def spain_only(self):
        return self.filter(kraj=Kraj.HISZPANIA) 
    def england_only(self):
        return self.filter(kraj=Kraj.ANGLIA)  
    def italy_only(self):
        return self.filter(kraj=Kraj.WŁOCHY)  
    def niemcy_only(self):
        return self.filter(kraj=Kraj.NIEMCY) 
    def france_only(self):
        return self.filter(kraj=Kraj.FRANCJA)
    


class FootballManager(models.Manager):
    def get_queryset(self):
        return FootballQuerySet(self.model, using=self._db)
    
    def polska(self):
        return self.get_queryset().poland_only()
    def włochy(self):
        return self.get_queryset().italy_only()
    def hiszpania(self):
        return self.get_queryset().spain_only()
    def anglia(self):
        return self.get_queryset().england_only()
    def francja(self):
        return self.get_queryset().france_only()
    def niemcy(self):
        return self.get_queryset().niemcy_only()
    

