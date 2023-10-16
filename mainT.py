from player import SelfPlayer
from trainers import trainers

player = SelfPlayer("gang")
#player.setName()
player.myPokemon()

trainer = trainers[0]

print(trainer.name)
for pokemon in trainer.pokemons: 
      print("Vos pokémon :", pokemon.name)
      print("State :", ['attaque :', pokemon.attack, 'defense :', pokemon.defense])
      print("Attaques :")
      for i in pokemon.attacks:
        print('- ', i.name)   