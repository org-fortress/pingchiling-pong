from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load("background.jpg"), (700,500))
score1 = 0
score2 = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", 15, self.rect.centerx - 6, self.rect.top, 15, 20)
        bullets.add(bullet)
class Ball(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__( player_image, player_speed, player_x, player_y, player_width, player_height)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def updateb(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
player = Player("racket.png", 5, 0, 250, 50, 150)
player1 = Player("racket1.png", 5, 650, 250, 50, 150)
ball = Ball("tennis ball.png", 2, 300,100,35,35)
font.init()
font1 = font.SysFont('Arial', 36)

clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        player1.update1()
        player1.reset()
        ball.updateb()
        ball.reset()
        text_player1 = font1.render('Счёт игрока 1: ' + str(score1), 1, (255,255,255))
        text_player2 = font1.render('Счёт игрока 2: ' + str(score2), 1, (255,255,255))
        player1_win = font1.render('ИГРОК 1 ПОБЕДИЛ!!!!!!!!!!!!!!', 1, (255,255,0))
        player2_win = font1.render('ИГРОК 2 ПОБЕДИЛ!!!!!!!!!!!!!!', 1, (255,255,0))
        window.blit(text_player1, (0,0))
        window.blit(text_player2, (428,0))
        if ball.colliderect(player.rect):
            ball.speed_x *= -1
        if ball.colliderect(player1.rect):
            ball.speed_x *= -1
        if ball.rect.y < 0 or ball.rect.y > 450:
            ball.speed_y *= -1
        if ball.rect.x > 700:
            score1 += 1
            ball.rect.x = randint(150,250)
            ball.rect.y = randint(150,250)
            ball.speed_x = randint(2,5)
            ball.speed_y = randint(2,5)
        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = randint(150,250)
            ball.rect.y = randint(150,250) 
            ball.speed_x = randint(2,5)
            ball.speed_y = randint(2,5)
        if score1 > 9:
            finish = True
            window.blit(player1_win, (200,200))
        if score2 > 9:
            finish = True
            window.blit(player2_win, (200,200))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_r]:
            score1 *= 0
            score2 *= 0
            ball.rect.x = 250
            ball.rect.y = randint(150,250)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
