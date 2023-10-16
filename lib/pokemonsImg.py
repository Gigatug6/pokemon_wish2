import pygame 

from lib.pokemons import pokemons

pokemons_artwork = []

for key in pokemons.keys():
  pokemons_artwork.append(pygame.image.load(f'./img/artwork/{str(key).zfill(3)}.png'))
