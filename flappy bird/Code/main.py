from settings import *
from UI import *
from ground import Ground
from pipes import MariosPipes
from Birb import PeskyBird

#! The game kinda jitters at times (Maybe it only jitters for me tho)
#! The jittering is not enough to cause any real problems but may just look weird, sorry
#! I don't want to fix it cuz like i know i have to rewrite some random part of the code and I'm feeling lazy fr
#! This game also uses pygame-ce and not base pygame 

class Game:
    def __init__(self):
        #* Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.collison_sprites = pygame.sprite.Group()
        self.pipe_sprites = pygame.sprite.Group()
        self.gameover = False

        self.running = True

        #* sprites
        #~ background
        self.background = pygame.image.load(join('sprites', 'background-day.png')).convert_alpha()
        self.background_rect = self.background.get_frect(topleft = (0, 0))
        #~ ground
        self.ground1 = Ground((self.all_sprites, self.collison_sprites), 0)
        self.ground2 = Ground((self.all_sprites, self.collison_sprites), 1)
        #* Sprite layering issue fixed itself idk how
        #~ Birb
        self.player = PeskyBird(self.all_sprites)
        #~ font
        self.score = Score(self.all_sprites)

        #* Audio load
        self.death_sound = pygame.mixer.Sound(join('audio', 'hit.wav'))
        self.point_sound = pygame.mixer.Sound(join('audio', 'point.wav'))

        #* Event
        self.spawn_pipe = pygame.event.custom_type()
        self.spawn_timer = pygame.time.set_timer(self.spawn_pipe, 1500)

    def collisions(self):
        #* My soul feels that this collison code is trash
        for sprite in self.collison_sprites:
            if pygame.sprite.collide_mask(self.player, sprite):
                self.gameover = True
                self.spawn_timer = pygame.time.set_timer(self.spawn_pipe, 0)
                if hasattr(sprite, 'ground'):
                    self.player.rect.bottom = WINDOW_HEIGHT - self.ground1.rect.height
                self.death_sound.play()
        for pipe in self.pipe_sprites:
            if pipe.rect.x < 50 and pipe.is_passed():
                self.score.value += 1
                self.point_sound.play()
                  
    def restart(self):
        #* Resetting
        self.score.value = 0
        self.player.kill()

        for sprite in self.pipe_sprites:
            sprite.kill()
        
        #* The following 3 lines feel like trash code
        for sprite in self.all_sprites: #? The only way i could find to remove gameover when gamestarts 😭😭
            if hasattr(sprite, 'gameover_attr'):
                sprite.kill()
        self.gameover = False

        #* Creating
        self.player = PeskyBird(self.all_sprites)
        self.spawn_timer = pygame.time.set_timer(self.spawn_pipe, 1500)

    def run(self):
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.spawn_pipe:
                    self.pipes = MariosPipes((self.all_sprites, self.collison_sprites, self.pipe_sprites))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_r and self.gameover:
                        self.restart()

            self.display_surface.blit(self.background, self.background_rect) #? Only 1 background no need for classes and stuff

            #* Update
            if not self.gameover:
                self.all_sprites.update(dt)  
                self.collisions()
            if self.gameover:
                self.gameoverUI = GameOverUI(self.score.value, (self.all_sprites))

            #* Draw
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()