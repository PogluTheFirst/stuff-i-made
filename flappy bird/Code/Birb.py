from settings import *

class PeskyBird(pygame.sprite.Sprite):
    def __init__(self, groups):
        self._layer = 3
        super().__init__(groups)

        self.frames = [
            pygame.image.load(join('animation', '0.png')).convert_alpha(),
            pygame.image.load(join('animation', '1.png')).convert_alpha(),
            pygame.image.load(join('animation', '2.png')).convert_alpha(),
        ]
        self.frame_index = 0
        self.animation_speed = 10

        self.image = self.frames[0]
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.gravity = 0

        #* audio
        self.jump_sound = pygame.mixer.Sound(join('audio', 'wing.wav'))

    def check_input(self):
        if pygame.key.get_just_pressed()[pygame.K_SPACE] or pygame.mouse.get_just_pressed()[0]:
            self.gravity = 0
            self.gravity = -7.15
            self.jump_sound.play()

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self, dt):
        self.check_input()
        self.animate(dt)
        self.gravity += GRAVITY
        self.rect.y += self.gravity
        if self.rect.top < -50: self.rect.top = -50


#! This is a bird:
#?⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀
#?⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀
#?⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣦⣄⡀
#?⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣾⣿⡿⠟⠉
#?⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
#?⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
#?⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
#?⢤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀
#?⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
#?⠀⠀⠀⠀⠉⠙⠻⠿⠿⣿⣿⣿⣿⣿⣯⣄⡀⠀⠀⠀⠀⠀
#?⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠛⠛⠻⢿⡿⠁⠀⠀⠀

#! This is not a bird:
#^⢰⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
#^⠀⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿
#^⠀⠘⢿⣿⣿⣿⣿⣦⣀⣀⣀⣄⣀⣀⣠⣀⣤⣶⣿⣿⣿⣿⣿⠇
#^⠀⠀⠈⠻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀
#^⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠋⠀⠀⠀
#^⠀⠀⠀⢠⣿⣿⡏⠆⢹⣿⣿⣿⣿⣿⣿⠒⠈⣿⣿⣿⣇⠀⠀⠀
#^⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣛⣻⣿⣿⣿⣶⣾⣿⣿⣿⣿⡀⠀⠀
#^⠀⠀⠀⡁⠀⠈⣿⣿⣿⣿⢟⣛⡻⣿⣿⣿⣟⠀⠀⠈⣿⡇⠀⠀
#^⠀⠀⠀⢿⣶⣿⣿⣿⣿⣿⡻⣿⡿⣿⣿⣿⣿⣶⣶⣾⣿⣿⠀⠀
#^⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
#^⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀