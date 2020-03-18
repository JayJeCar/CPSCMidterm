import pygame

class Ship:  
  def __init__(self, vector = Vector()): 
    self.screen = screen
    self.velocity = vector
    self.screen_rect = game.screen.get_rect()
    self.image = pg.image.load("someship.png") #I do not have this image saved to my files, but we would just download an image and save it in the images folder as someship.png
    
  def center_ship(self): 
    self.rect = self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom
    r = self.rect
    return 'Ship({}, {}), v={}'.format(r.x, r.y, self.velocity)
    
  def fire(self): pass
    #laser = Laser #Assuming the Laser class exists
    
  def remove_lasers(self): pass 
    #self.lasers.remove()
  
  def move(self): 
    if self.velocity == Vector()
      return #updating position
    self.rect.left += self.velocity.x
    self.rect.top += self.velocity.y
  
  def draw(self): 
    
  
  def update(self): pass
    self.move()
    self.draw()
  
  class Vector:  
    def __init__(self): pass   
    
    def __repr__(self):     
      return “Vector ({}, {})”.format(self.x, self.y)  
    
    def __add__(self, other): pass  
    
    def __sub__(self, other): pass 
    
    def __rmul__(self, k: float): pass 
    
    def __mul__(self, k: float): pass 
    
    def __truediv__(self, k: float): pass 
    
    def __neg__(self): pass  
    
    def __eq__(self): pass 
    
@staticmethod 
def test():          
# feel free to change the test code  
  v = Vector(x=5, y=5)  
  u = Vector(x=4, y=4)  
  print(‘v is {}’.format(v))  
  print(‘u is {}’.format(u))  
  print(‘uplusv is {}’.format(u + v))  
  print(‘uminusv is {}.format(u – v))  
  print(‘ku is {}’.format(3 * u))  
  print(‘-u is {}’.format(-1 * u))
  
def main():   
  Vector.test()
