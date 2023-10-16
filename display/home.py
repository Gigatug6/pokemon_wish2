import pygame as pg

from utils.settings import *

from utils.style import StylePygam

from lib.pokemons import pokemons
from lib.pokemonsImg import pokemons_artwork

stylePygam = StylePygam(pg)

class DisplayHome:
  def __init__(self, game):
    self.game = game

    self.playerName =  stylePygam.getFont("Arial", 40).render(self.game.player.name, True, (255, 255, 255))

    self.y = 50
    self.x = 10
    self.index_select = 1

    self.totalPokemons = len(pokemons.keys())

  def fram_bool(self, fram):
    if self.game.timer % fram == 0:
        return False
    return True

  def check_events(self):
    for event in pg.event.get():
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
          self.index_select += 1
        elif event.key == pg.K_LEFT:
          self.index_select -= 1
        elif event.key == pg.K_DOWN:
          self.index_select -= 10
        elif event.key == pg.K_UP:
          self.index_select += 10    
        if(self.index_select > self.totalPokemons):
          self.index_select = 1
        elif(self.index_select < 1):
          self.index_select = self.totalPokemons

        if event.key == pg.K_RETURN:
          self.game.player.pokemons.append(pokemons[self.index_select]) 


  def draw(self):
    label_selectPokemon = stylePygam.getFont("Arial", 20).render(f"Sélectionnez un pokemon ({len(self.game.player.pokemons)}/{self.game.player.totalPokemons}):", True, (255, 255, 255))
    self.game.screen.blit(label_selectPokemon, (5, self.y))

    y2 = self.y
    x2 = self.x
    self.game.screen.blit(self.playerName, (int(WIDTH//2), 0))

    for pokemon in self.game.player.pokemons:
      name_pokemon = stylePygam.getFont("Arial", 20).render(f"({str(pokemon.index).zfill(3)}) " + pokemon.name, True, (255, 255, 255))
      self.game.screen.blit(name_pokemon, (self.x, self.y + 25))
      self.game.screen.blit(pokemons_artwork[pokemon.index - 1], (self.x, self.y + 50))
      self.x += 200

    if(len(self.game.player.pokemons) < self.game.player.totalPokemons):
      name_pokemon = stylePygam.getFont("Arial", 20).render(f"({str(self.index_select).zfill(3)}) " + pokemons[self.index_select].name, True, (255, 255, 255))
      self.game.screen.blit(name_pokemon, (self.x, self.y + 25))
      self.game.screen.blit(pokemons_artwork[self.index_select - 1], (self.x, self.y + 50))
      if self.fram_bool(5):
        pg.draw.rect(self.game.screen, (255, 255, 255), (self.x + 20, self.y + 200, 100, 2))

      

    self.y = y2  
    self.x = x2