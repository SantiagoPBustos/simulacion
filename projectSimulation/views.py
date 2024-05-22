from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from simulation.models import Character, BattleSimulator

# start_battle(): Inicia una nueva batalla creando instancias
# de los personajes con los datos proporcionados.

simulator = None


class StartBattle(APIView):

    def start_battle(self, request):
        global simulator
        data = request.json
        character1_data = data['character1']
        character2_data = data['character2']

        character1 = Character(**character1_data)
        character2 = Character(**character2_data)

        simulator = BattleSimulator(character1, character2)

        response = JsonResponse(
            {"message": "Battle started", "status": "success"})

        return response


class SimulateRound(APIView):

    # simulate_round(): Simula una ronda de batalla y
    # devuelve el resultado en formato JSON.
    def simulate_round():
        global simulator
        if not simulator:
            return JsonResponse({"message": "No battle in progress", "status": "error"})

        round_result = simulator.simulate_round()
        result = JsonResponse(round_result)
        return result
