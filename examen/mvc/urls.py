from django.urls import path
from mvc import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toaltadept', views.toaltadept, name='toaltadept'),
    path('altadeptexe', views.altadeptexe, name='altadeptexe'),
    path('toeditardept', views.toeditardept, name='toeditardept'),
    path('editardeptexe', views.editardeptexe, name='editardeptexe'),
    path('borrardept', views.borrardept, name='borrardept'),
]
