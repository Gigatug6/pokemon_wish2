from pokemons import pokemons

class Player:
  def __init__(self, name:str, totalPokemons:int):
    self.name = name
    self.pokemons = [pokemons[1], pokemons[7]]
    self.totalPokemons = min(6, totalPokemons)
    self.pokemons:list[pokemons] = []


  """
  def setName(self):
    self.name = input("Name : ")

  def myPokemon(self):
    for pokemon in self.pokemons: 
      print("Vos pokémon :", pokemon.name)
      print("State :", ['attaque :', pokemon.attack, 'defense :', pokemon.defense])
      print("Attaques :")
      for i in pokemon.attacks:
        print('- ', i.name)   
  """
