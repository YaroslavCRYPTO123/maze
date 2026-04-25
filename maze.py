from pygame import *
mixer.init()
mixer.music.load('redball_Sound.mp3')
mixer.music.play()
font.init()
window = display.set_mode((700,500))
display.set_caption('maze')
bg = transform.scale(image.load('background.png'),(700,500))
clock = time.Clock()
FPS = 60
speed = 10
game = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


treasure = GameSprite('star.png',600,425,0)
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 425:
            self.rect.y += speed

hero = Player('redball.png',0,425,8)
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x > 700 - 65:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
cyborg = Enemy('monster.png',625,250,2)
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
wall_1 = Wall(255,126,0,100,0,15,350)
wall_2 = Wall(255,126,0,225,150,15,350)
wall_3 = Wall(255,126,0,350,0,15,350)
wall_4 = Wall(255,126,0,460,80,15,450)
finish = False
font = font.SysFont('Arial', 70)
win = font.render('You win!',True,(0,255,33))
loss = font.render('Game over!',True,(255,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(bg,(0,0))
    hero.reset()
    cyborg.reset()
    treasure.reset()
    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()
    wall_4.draw_wall()
    
    if finish != True:
        hero.update()
        cyborg.update()
        if sprite.collide_rect(hero, treasure):
            finish = True
            result = 'win'
        if sprite.collide_rect(hero, cyborg):
            finish = True
            result = 'loss'
        if sprite.collide_rect(hero, wall_1) or sprite.collide_rect(hero, wall_2) or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4):
            finish = True
            result = 'loss'

    if finish == True:
        if result == 'win':
            window.blit(win,(200,200))
        elif result == 'loss':
            window.blit(loss,(200,200))
    
    clock.tick(FPS)
    display.update()
    #завершение
