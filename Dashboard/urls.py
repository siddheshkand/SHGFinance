from django.urls import path, include
from Dashboard import views

urlpatterns = [
    path('', views.dashboard)
]
