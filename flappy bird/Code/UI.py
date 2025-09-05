from settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self, groups):
        self._layer = 4
        super().__init__(groups)
        self.value = 0
    
    def create_score(self):
        self.font = pygame.font.Font(join('sprites', 'font.ttf'), 20)
        self.font_surf = self.font.render(str(self.value), False, "#EBE1E1")
        self.font_rect = self.font_surf.get_frect()

        self.image = pygame.surface.Surface((self.font_rect.width, self.font_rect.height), pygame.SRCALPHA)
        self.image.blit(self.font_surf, self.font_rect)
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH // 2, 50))

    def update(self, _):
        self.create_score()

class GameOverUI(pygame.sprite.Sprite):
    def __init__(self, score, groups):
        #* setup
        self._layer = 4
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.score = score
        self.gameover_attr = True

        #* surf
        self.gameover_png = pygame.image.load(join('sprites', 'gameover.png')).convert_alpha()
        self.gameover_png_rect = self.gameover_png.get_frect(topleft = (0, 0))

        #* font
        self.font = pygame.font.Font(join('sprites', 'font.ttf'), 18)
        self.font_surf = self.font.render(f'Score:  {self.score}', False, "#ca694b")
        self.font_rect = self.font_surf.get_frect(midleft = (10, 73))

        self.info_font = pygame.font.Font(join('sprites', 'font.ttf'), 15)
        self.info = self.info_font.render('R to restart', True, '#000000')
        self.info_rect = self.info.get_frect(midleft = (10, 113))

        #* Scoring
        self.score_rect = pygame.FRect((0, 50), (192, 42))

        #* Surface to place
        self.image = pygame.surface.Surface((200, 150), pygame.SRCALPHA)
        self.image.blit(self.gameover_png, self.gameover_png_rect)
        pygame.draw.rect(self.image, '#DED895', self.score_rect, 0, 4)
        pygame.draw.rect(self.image, '#543847', self.score_rect, 2, 4)
        self.image.blit(self.font_surf, self.font_rect)
        self.image.blit(self.info, self.info_rect)
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 - 75))

    def update(self, _):
        pass