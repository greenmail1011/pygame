# 操控 sqrite
import pygame
#遊戲初始化 and 創建視窗
FPS = 60
WIDTH = 500
HEIGHT = 600

WHITE = (255,255,255)
GREEN = (0,255,0)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("第一個遊戲")
clock =pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() #定位
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
        #self.rect.x += 2
        #if self.rect.left > WIDTH:
            #self.rect.right = 0
            

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
        
#遊戲迴圈
running = True
while running:
    clock.tick(FPS) #1秒之內最多只能執行FPS次
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    all_sprites.update()
    
    #畫面顯示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()