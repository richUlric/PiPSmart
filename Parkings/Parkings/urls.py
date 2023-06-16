"""
URL configuration for Parkings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path 
from Parking import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('accueil/', views.my_viewA, name='accueil'),
    path('reservation/', views.my_viewB, name='reservation'), 
    path('Connexion/', views.my_viewC, name='Connexion'), 
    path('tarifs/', views.my_viewD, name='tarifs'), 
    path('contact/', views.my_viewE, name='contact'),
    path('enregistrer/', views.my_viewG, name='enregistrer'),  
    path('paiement/', views.my_viewI, name='paiement'),
    path('success/', views.my_viewJ, name='my_viewJ'),
    path('admin/', admin.site.urls), 
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
