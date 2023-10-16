import pygame as pg
import sys

from utils.settings import *
from utils.style import StylePygam
from utils.menu import EnumMenu

from display.home import DisplayHome

from lib.player import Player

stylePygam = StylePygam(pg)

class Game:
  def __init__(self):
    pg.init()
    #pg.mouse.set_visible(False)
    self.screen = pg.display.set_mode(RES)
    #pg.event.set_grab(True)
    self.clock = pg.time.Clock()
    self.delta_time = 1
    self.global_trigger = False
    self.global_event = pg.USEREVENT + 0
    pg.time.set_timer(self.global_event, 40)
    self.new_game()
    self.menu = EnumMenu.Home

    #self.x = 10

    self.player = Player("Gigatug6", PLAYER_POKEMON)

    self.displayHome = DisplayHome(self)

  def new_game(self):
    pass  

  def check_events(self):
    self.global_trigger = False
    for event in pg.event.get():
      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
        pg.quit()
        sys.exit()
      """elif event.type == pg.KEYDOWN:
        if event.key == pg.K_d:
          self.x = self.x + 10  """

  def update(self):
    self.delta_time = self.clock.tick(FPS)
    pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

  def draw(self):
    self.screen.fill("black")
    #label1 = stylePygam.getFont("Arial", 40).render("TEST", True, (255, 255, 255))
    #self.screen.blit(label1, (0, 0))   

    self.displayHome.draw()  
 
    pg.display.update()

  def run(self):
    while True:
      self.check_events()
      self.update()
      self.draw()



if __name__ == "__main__":
  game = Game()
  game.run()  