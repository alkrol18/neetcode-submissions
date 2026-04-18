class Pet:
    def __init__(self, name: str, species: str, health: str = None, speed: int = None):
        self.name = name
        self.species = species
        self.health = health
        self.speed = speed



# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
