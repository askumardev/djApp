from django.urls import path
from . import views


urlpatterns = [
    # path('january/', views.january),
    # path('any_month/', views.any_month),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge)
]