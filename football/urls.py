
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers 
from footballweb.views import UserView, FootballView, wysylka_mail
from django.contrib.auth.views import (PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView)



router = routers.DefaultRouter() 
router.register(r'users', UserView)
router.register(r'football', FootballView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('football/', include('footballweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),    
    path('register/', wysylka_mail, name="register"),    
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),    
    path('password_reset_done', PasswordChangeDoneView.as_view(), name='password_reset_done'),    
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),    
    path('password_reset_complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),    
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


