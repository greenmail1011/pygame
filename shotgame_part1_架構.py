import pygame
#遊戲初始化 and 創建視窗
FPS = 60
WHITE = (255,255,255)
WIDTH = 500
HEIGHT = 600
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
clock =pygame.time.Clock()

#遊戲迴圈
while running:
    clock.tick(FPS) #1秒之內最多只能執行FPS次
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    
    #畫面顯示
    screen.fill(WHITE)
    pygame.display.update()

pygame.quit()