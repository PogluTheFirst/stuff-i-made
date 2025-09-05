from settings import *
from random import uniform

class MariosPipes(pygame.sprite.Sprite):
    def __init__(self, groups):
        #* setup
        self._layer = 0
        super().__init__(groups)

        self.floor_height = pygame.image.load(join('sprites', 'base.png')).get_frect().height
        self.gap = 100
        min_y = 100
        max_y = WINDOW_HEIGHT - self.floor_height - 100

        #* pipes
        self.pipe_sprite = pygame.image.load(join('sprites', 'pipe_green.png')).convert_alpha()
        self.pipe_sprite_rect = self.pipe_sprite.get_frect()

        #^ Pipes get created seperately but are combined into single surface to be placed
        self.top_pipe = pygame.transform.flip(self.pipe_sprite, False, True)
        self.top_pipe_rect = self.top_pipe.get_frect(topleft = (0, 0))

        self.bottom_pipe = self.pipe_sprite
        self.bottom_pipe_rect = self.bottom_pipe.get_frect(topleft = (0, self.pipe_sprite_rect.height + self.gap))

        self.image = pygame.surface.Surface((self.pipe_sprite_rect.width, self.pipe_sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)
        self.image.blit(self.top_pipe, self.top_pipe_rect)
        self.image.blit(self.bottom_pipe, self.bottom_pipe_rect)
        self.rect = self.image.get_frect(midleft = (WINDOW_WIDTH, uniform(min_y, max_y)))
        self.mask = pygame.mask.from_surface(self.image)

        self.passed_player = False

    def move(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.kill()

    def is_passed(self): #? Used in main.py
        if self.rect.x < 50 and not self.passed_player:
            self.passed_player = True
            return True
        return False

    def update(self, _):
        self.move()