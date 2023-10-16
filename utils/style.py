import pygame

class StylePygam:
  allowed_colors = ('black', 'white', 'green', 'red', 'blue')
  allowed_fonts = ('Arial')

  def __init__(self, pygame:pygame):
    self.pygame = pygame

  def getColor(self, color:str):
    if color not in self.allowed_colors:
      return self.pygame.Color(0, 0, 0)
    elif color == 'black':
      return self.pygame.Color(0, 0, 0)  
    elif color == 'white':
      return self.pygame.Color(255, 255, 255)  
    elif color == 'green':
      return self.pygame.Color(0, 255, 0)    
    elif color == 'red':
      return self.pygame.Color(255, 0, 0)  
    elif color == 'blue':
      return self.pygame.Color(0, 0, 255) 
    
  def getFont(self, font:str, size:int):
    if font not in self.allowed_fonts:
      return self.pygame.font.SysFont('Arial', 40)
    else:
      return self.pygame.font.SysFont(font, size if size else 40)