from settings import *

#* Two grounds are gonna be used to keep the moving effect so i'll make a class for proper order

class Ground(pygame.sprite.Sprite):
    def __init__(self, groups, index):
        self._layer = 1
        super().__init__(groups)

        self.index = index
        
        self.image = pygame.image.load(join('sprites', 'base.png')).convert_alpha()
        self.rect = self.image.get_frect(bottomleft = (WINDOW_WIDTH * self.index, WINDOW_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.ground = True

    def move(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH 
            
    def update(self, _):
        self.move()