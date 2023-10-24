from django.urls import path, include
from .views import Homepage, Homefilmes

urlpatterns = [
    path('', Homepage.as_view()),
    path('homefilmes', Homefilmes.as_view()),
] 