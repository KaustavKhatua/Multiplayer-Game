import pygame

width = 500
height = 400

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = 1
        if keystate[pygame.K_UP]:
            self.speedy = -1
        if keystate[pygame.K_DOWN]:
            self.speedy = 1
        
        self.rect.centerx = self.rect.centerx + self.speedx
        self.rect.centery = self.rect.centery + self.speedy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    all_sprites.update()

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(120)