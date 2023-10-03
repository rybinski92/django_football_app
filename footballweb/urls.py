from django.urls import path
from footballweb.views import wszystkie_football, nowy_fc, edytuj_fc, usun_fc, contact
from . import views

urlpatterns = [
    path('wszystkie/', wszystkie_football, name="wszystkie_football"),
    path('nowy/', nowy_fc, name="nowy_fc"),
    path('edytuj/<int:id>/', edytuj_fc, name="edytuj_fc"),
    path('usun/<int:id>/', usun_fc, name="usun_fc"),
    path('contact/', contact, name="contact"),    
    path('wyszukiwarka/', views.wyszukiwarka, name='wyszukiwarka'),
    path('register/', views.register, name='register')
    
]
