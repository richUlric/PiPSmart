from django.urls import path 
from . import views 
from .views import my_viewA
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('accueil/',my_viewA, name='accueil'),
    path('reservation/', views.my_viewB, name='reservation'), 
    path('Connexion/', views.my_viewC, name='Connexion'), 
    path('tarifs/', views.my_viewD, name='tarifs'), 
    path('contact/', views.my_viewE, name='contact'),
    path('enregistrer/', views.my_viewF, name='enregistrer'), 
    path('enregistrer/', views.my_viewG, name='enregistrer'), 
    path('paiement/', views.my_viewI, name='paiement'), 
    path('success/', views.my_viewJ, name='success'), 
    path('qr_code/', views.generate_qr_code, name='generate_qr_code'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
