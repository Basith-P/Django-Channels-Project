from django.urls import path

from .views import dashboard, main

app_name = 'stats'

urlpatterns = [
    path('', main, name='main'),
    path('<slug:slug>/', dashboard, name='dashboard'),
]
