from django.shortcuts import render, get_object_or_404, redirect
from .models import Football
from .forms import FcForm, WyszukiwarkaForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from django.contrib.auth.models import User 
from .serializers import UserSerializer, FootballSerializer
from django import forms
from django.http import HttpResponse
from django.core.mail import send_mail


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FootballView(viewsets.ModelViewSet):
    queryset = Football.objects.all()
    serializer_class = FootballSerializer


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


def wszystkie_football(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    wszystkie = Football.objects.all()
    # wszystkie = []
    return render(request, 'football.html', {'football': wszystkie})

def content(request):
    return render(request, 'content.html', {'content': content})

@login_required
def nowy_fc(request):

    form_fc = FcForm(request.POST or None, request.FILES or None)    

    if form_fc.is_valid():
        ball = form_fc.save(commit=False)
        ball.save() 

        return redirect(wyszukiwarka)

    return render(request, 'fc_form.html', {'form': form_fc, 'nowy': True}) 

@login_required
def edytuj_fc(request, id):

    football = get_object_or_404(Football, pk=id)  


    form_fc = FcForm(request.POST or None, request.FILES or None, instance=football)    

    if form_fc.is_valid():
        ball = form_fc.save(commit=False)

        ball.save() 

        return redirect(wyszukiwarka)

    return render(request, 'fc_form.html', {'form': form_fc,  'nowy': False}) 

@login_required
def usun_fc(request, id):
    football = get_object_or_404(Football, pk=id)

    if request.method == "POST":
        football.delete()
        return redirect(wszystkie_football)


    return render(request, 'potwierdz.html', {'football': football}) 



def wyszukiwarka(request):
    kluby = Football.objects.all()
    form = WyszukiwarkaForm(request.GET)

    if form.is_valid():
        kraj = form.cleaned_data['kraj']
        if kraj and kraj != 'wszystkie':
            kluby = kluby.filter(kraj=kraj)

    return render(request, 'wyszukiwarka.html', {'kluby': kluby, 'form': form})



def contact(request):

    return render(request, 'contact.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Logowanie użytkownika po rejestracji
            login(request, user)
            return redirect('wszystkie_football')  # Przekieruj użytkownika na stronę główną po rejestracji
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def wysylka_mail(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Wysłanie wiadomości powitalnej na adres e-mail
            email = form.cleaned_data['email']
            wiadomosc = "Witamy na naszej stronie InstaFootball. Cieszymy się, że jesteś z nami."
            send_mail(
                "Tutaj InstaFootball :)",
                wiadomosc,
                'adamrybinski.kontakt@gmail.com',
                [email],
                fail_silently=False
            )
            # ... kod do wysłania wiadomości e-mail ...
            return redirect('wszystkie_football')  # Przekierowanie po udanej rejestracji
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})