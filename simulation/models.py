from simulation.generate_numbers import box_muller, LinearCongruentialGenerator

# Character: Esta clase representa a un personaje en el juego.


class Character:
    def __init__(self, name, health, mean_attack, std_attack, mean_defense, std_defense, seed):
        self.name = name
        self.health = health
        self.mean_attack = mean_attack
        self.std_attack = std_attack
        self.mean_defense = mean_defense
        self.std_defense = std_defense
        # Generador de números pseudoaleatorios
        self.lcg = LinearCongruentialGenerator(seed)

    # generate_attack(): Genera un valor de ataque usando el método Box-Muller.
    def generate_attack(self):
        attack, _ = box_muller(self.mean_attack, self.std_attack, self.lcg)
        return max(0, attack)

    # generate_defense(): Genera un valor de defensa usando el método Box-Muller.
    def generate_defense(self):
        defense, _ = box_muller(self.mean_defense, self.std_defense, self.lcg)
        return max(0, defense)

    # take_damage(damage): Reduce la salud del personaje en función del daño recibido.
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # is_alive(): Verifica si el personaje sigue vivo.
    def is_alive(self):
        return self.health > 0

# BattleSimulator: Esta clase maneja la simulación de una batalla entre dos personajes.


class BattleSimulator:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    # simulate_round(): Simula una ronda de ataque y defensa entre los dos personajes.
    def simulate_round(self):
        attack_c1 = self.character1.generate_attack()
        defense_c2 = self.character2.generate_defense()
        damage_to_c2 = max(0, attack_c1 - defense_c2)

        attack_c2 = self.character2.generate_attack()
        defense_c1 = self.character1.generate_defense()
        damage_to_c1 = max(0, attack_c2 - defense_c1)

        self.character2.take_damage(damage_to_c2)
        self.character1.take_damage(damage_to_c1)

        return {
            "character1": {
                "name": self.character1.name,
                "health": self.character1.health,
                "is_alive": self.character1.is_alive()
            },
            "character2": {
                "name": self.character2.name,
                "health": self.character2.health,
                "is_alive": self.character2.is_alive()
            }
        }
