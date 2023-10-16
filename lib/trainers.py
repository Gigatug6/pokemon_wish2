import random
from lib.pokemons import pokemons, SetPokemon

class SetTrainer:
  def __init__(self, name, totalPokemons):
    self.name = name
    self.totalPokemons = totalPokemons
    self.pokemons:list[SetPokemon] = []
    for i in range(self.totalPokemons):
      self.__setPokemons()
    
  def __setPokemons(self):
    key = random.choice(list(pokemons.keys()))
    self.pokemons.append(pokemons[key])

trainers = {
  0: SetTrainer("Cynthia", 2)
}  