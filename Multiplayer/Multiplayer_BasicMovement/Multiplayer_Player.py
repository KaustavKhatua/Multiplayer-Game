import socket
import pygame

server_ip = '127.0.0.1'
server_port = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))

positions = s.recv(1024).decode("utf-8")
player1_position_x = int(positions.split('/')[0].split(',')[0])
player1_position_y = int(positions.split('/')[0].split(',')[1])
player2_position_x = int(positions.split('/')[1].split(',')[0])
player2_position_y = int(positions.split('/')[1].split(',')[1])

pygame.init()

width = 500
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class You(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.x = player1_position_x
        self.rect.y = player1_position_y

        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.speedx = 0
        self.speedy = 0

        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_LEFT]:
            self.speedx = -2
        if key_state[pygame.K_RIGHT]:
            self.speedx = 2
        if key_state[pygame.K_UP]:
            self.speedy = -2
        if key_state[pygame.K_DOWN]:
            self.speedy = 2
        
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        
        self.current_position = f'{self.rect.x},{self.rect.y}'
        s.sendall(self.current_position.encode())

class Him(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = player2_position_x
        self.rect.y = player2_position_y

    def update(self):
        data = s.recv(1024).decode("utf-8")
        self.rect.x = int(data.split(',')[0])
        self.rect.y = int(data.split(',')[1])

all_players = pygame.sprite.Group()
you = You()
all_players.add(you)
him = Him()
all_players.add(him)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    all_players.update()

    screen.fill((0, 0, 0))
    
    all_players.draw(screen)

    pygame.display.flip()

    clock.tick(60)
