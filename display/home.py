import pygame as pg

from utils.settings import *

from utils.style import StylePygam

from lib.pokemons import pokemons

stylePygam = StylePygam(pg)

class DisplayHome:
  def __init__(self, game):
    self.game = game

    self.playerName =  stylePygam.getFont("Arial", 40).render(self.game.player.name, True, (255, 255, 255))

    self.label_selectPokemon = stylePygam.getFont("Arial", 20).render("Sélectionnez un pokemon :", True, (255, 255, 255))

    self.cursor_y = 50
    self.index_select = 1

  def update(self):
    pass  

  def draw(self):
    old_cursor = self.cursor_y
    self.game.screen.blit(self.playerName, (int(WIDTH/2), 0))

    for pokemon in self.game.player.pokemons:
      self.cursor_y += 50

    if(len(self.game.player.pokemons) < self.game.player.totalPokemons):
      self.game.screen.blit(self.label_selectPokemon, (0, self.cursor_y))
      name_pokemon = stylePygam.getFont("Arial", 20).render(pokemons[self.index_select].name, True, (255, 255, 255))
      self.game.screen.blit(name_pokemon, (0, self.cursor_y + 25))


    self.cursor_y = old_cursor  