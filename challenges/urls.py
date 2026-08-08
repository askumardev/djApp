from django.urls import path
from . import views


urlpatterns = [
    # path('january/', views.january),
    # path('any_month/', views.any_month),
    path('', views.index, name='index'),
    path('<int:month>/', views.monthly_challenge_by_number, name='monthly-challenge-by-number'),
    path('<str:month>/', views.monthly_challenge, name='monthly-challenge'),
]