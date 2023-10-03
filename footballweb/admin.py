from django.contrib import admin
from .models import Football

# admin.site.register(Football)

@admin.register(Football)
class FootballAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = "opis"
    list_display = ["tytul", "rok"]
    list_filter = ("lig_mistrzów",)
    search_fields = ("tytul",)




