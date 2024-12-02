from pygame import *

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 5:
            self.rect.x -+ self.speed
        if keys[K_d] and self.rect.x <= win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption("Shoot!")
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

Player = player("rocket.png", 5, win_width - 100, 80, 100, 4)

run = True
clock = time.Clock()
fps = 60

game = True
finish = False

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        Player.update()

        Player.reset()

        display.update()
    time.delay(50)

