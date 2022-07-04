from django.urls import path
from . import views

urlpatterns = [
     path('', views.home),
     path('benefits/',views.benefits,name='benefits'),
     path('contacts/',views.contacts,name='contacts'),
     path('services/',views.services,name='services'),
     path('meetme/',views.meetme,name='meetme'),
     path('contactme/',views.contactme,name='contactme'),
     path('contacts/contactme/',views.contactmee,name='contactmee'),
     
     
     
    
]