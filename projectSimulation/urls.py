from django.urls import path
from .views import StartBattle, SimulateRound

urlpatterns = [
    path('start_battle/', StartBattle.as_view(), name='StartBattle'),
    path('simulate_round/', SimulateRound.as_view(), name='SimulateRound'),
]
