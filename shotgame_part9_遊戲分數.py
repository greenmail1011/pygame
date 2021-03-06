# 遊戲分數
import pygame                                                      
import random
import os
#遊戲初始化 and 創建視窗
FPS = 60
WIDTH = 500
HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()
 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("第一個遊戲")
clock =pygame.time.Clock()

#載入圖片
background_img = pygame.image.load(os.path.join("img","background.png")).convert()
player_img = pygame.image.load(os.path.join("img","player.png")).convert()
rock_img = pygame.image.load(os.path.join("img","rock.png")).convert()
bullet_img = pygame.image.load(os.path.join("img","bullet.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img", f"rock{i}.png")).convert())

font_name = pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        #dself.image.fill(GREEN)
        self.rect = self.image.get_rect() #定位
        self.radius = 20
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        #self.rect.x = 200
        #self.rect.y = 200
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10 
        self.speedx = 8
        
    def update(self):
        key_prssed = pygame.key.get_pressed() #按鍵是否按下
        if key_prssed[pygame.K_d]: #按下向右鍵
            self.rect.x += self.speedx
        if key_prssed[pygame.K_a]:  #按下向左鍵
            self.rect.x -= self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
         
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)
        self.image = self.image_ori.copy()
        self.image_ori.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #定位
        self.radius = int(self.rect.width * 0.85 / 2)
        #pygame.draw.circle(self.image,RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,WIDTH-self.rect.width)
        self.rect.y = random.randrange(-180,-100)
        self.speedy = random.randrange(2,10)
        self.speedx = random.randrange(-3,3)
        self.total_degree = 0
        self.rot_degree = 3
    
    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori,self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def update(self):
        self.rotate()
        self.rect.y += self.speedy 
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0,WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(2,10)
            self.speedx = random.randrange(-3,3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #定位
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        
        
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.bottom < 0:
            self.kill()
            
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets =pygame.sprite.Group()
player = Player()
all_sprites.add(player)
rock = Rock()
all_sprites.add(rock)
for i in range(8):
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)
score = 0       
#遊戲迴圈
running = True
while running:
    clock.tick(FPS) #1秒之內最多只能執行FPS次
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                
    #更新遊戲
    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True) #回傳字典
    for hit in hits:
        score += hit.radius
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)
        
    hits = pygame.sprite.spritecollide(player, rocks, False,pygame.sprite.collide_circle)
    if hits:
        running = False
    
        
    #畫面顯示
    screen.fill(BLACK)
    screen.blit(background_img,(0,0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    pygame.display.update()

pygame.quit()