from django.urls import path #On importe la classe 'path' du fichier urls.py du projet inventoryproject 
from . import views  #On importe le fichier view de dashboard

#Ce fichier va contenir toutes les urls de l'application dashboard

urlpatterns = [
    path('', views.index, name='index'),  #Page d'acceuil de l'application
    path('staff/', views.staff, name='staff')
]