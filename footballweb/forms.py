from django.forms import ModelForm 
from .models import Football
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FcForm(ModelForm):
    class Meta:
        model = Football
        fields = ['tytul', 'opis', 'rok', 'lig_mistrzów', 'logo', 'kraj']


class WyszukiwarkaForm(forms.Form):
    KRAJE = (
        ('', 'Wybierz...'),
        # ('wszystkie', 'Pokaż wszystkie wyniki'),
        (0, 'Hiszpania'),
        (1, 'Anglia'),
        (2, 'Włochy'),
        (3, 'Niemcy'),
        (4, 'Francja'),
        (5, 'Polska'),
        (6, 'Nieznany'),
    )

    kraj = forms.ChoiceField(choices=KRAJE, required=False)


