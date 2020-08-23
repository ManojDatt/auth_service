"""AuthService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import oauth2_provider.views as oauth2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    # path('token/', oauth2_views.TokenView.as_view(), name="token"),
    # path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
    path('users/', include('authapp.urls')),

]
