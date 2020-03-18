import pygame as pg


class Ship:

    def __init__(self, vector=Vector()):
        self.screen = screen
        self.velocity = vector
        self.screen_rect = game.screen.get_rect()
        self.image = pg.image.load("someship.png")  # I do not have this image saved to my files, but we would just download an image and save it in the images folder as someship.png

    def center_ship(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        r = self.rect
        return 'Ship({}, {}), v={}'.format(r.x, r.y, self.velocity)

    def fire(self): pass
    # laser = Laser #Assuming the Laser class exists

    def remove_lasers(self): pass
    # self.lasers.remove()

    def move(self):
        if self.velocity == Vector():
            return  # updating position

        self.rect.left += self.velocity.x

        self.rect.top += self.velocity.y

    def draw(self): pass

    def update(self):
        self.move()
        self.draw()


class Vector:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self): pass

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __rmul__(self, k: float): 
        return Vector(k * self.x, k * self.y)

    def __mul__(self, k: float): pass

    def __truediv__(self, k: float): pass

    def __neg__(self): 
        self.x *= -1
        self.y *= -1

    def __eq__(self): 
        return self.x == other.x and self.y == other.y


@staticmethod
def test():
    # feel free to change the test code

    v = Vector(x=5, y=5)

    u = Vector(x=4, y=4)

    #print(‘v is {}’.format(v))

    #print(‘u is {}’.format(u))

    #print(‘uplusv is {}’.format(u + v))

    #print(‘uminusv is {}.format(u – v))

    #print(‘ku is {}’.format(3 * u))

    #print(‘-u is {}’.format(-1 * u))

def main():
    Vector.test()
