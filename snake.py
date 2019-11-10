import socket, pygame, time, random
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode ((500,500))
font=pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption("REEEEE")
xmove=0
ymove=0
class Player:
    def __init__(self):
        self.coordinates=[[250,250]]
    def moveBy (self, x_distance, y_distance):
        time.sleep(0.1)
        if x_distance < 0:
            self.coordinates.insert(0,[self.coordinates[0][0]-13,self.coordinates[0][1]])
            self.coordinates.pop()
        elif x_distance > 0:
            self.coordinates.insert(0,[self.coordinates[0][0]+13,self.coordinates[0][1]])
            self.coordinates.pop()
        elif y_distance < 0:
            self.coordinates.insert(0,[self.coordinates[0][0],self.coordinates[0][1]-13])
            self.coordinates.pop()
        elif y_distance > 0:
            self.coordinates.insert(0,[self.coordinates[0][0],self.coordinates[0][1]+13])
            self.coordinates.pop()
    def draw(self):
        for p in range(len(self.coordinates)):
            pygame.draw.rect(window,(255,0,0),(self.coordinates[p][0],self.coordinates[p][1],20,20))
def message_display(text,textx,texty):
    textcontent = font.render (text, True, (255,0,0))
    textRect=textcontent.get_rect()
    textRect.center = (textx,texty)
    window.blit(textcontent,textRect)
def ateapple (score):
    score+=1
player1=Player()
score=0

x=random.randint(50,100)
y=random.randint(50,100)

while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                ymove= -1
                xmove=0
            elif event.key==K_DOWN:
                ymove = 1
                xmove=0
            elif event.key==K_LEFT:
                xmove = -1
                ymove = 0
            elif event.key==K_RIGHT:
                xmove= 1
                ymove = 0
    player1.moveBy(xmove,ymove)
    if player1.coordinates[0][1]< y <player1.coordinates[0][1]+20 and x-5<player1.coordinates[0][0]+20<x+5 or  player1.coordinates[0][0]< x < player1.coordinates[0][0]+20 and y-5<player1.coordinates[0][1]+20<y+5 or player1.coordinates[0][1]< y <player1.coordinates[0][1]+20 and x+7< player1.coordinates[0][0]< x+17 or player1.coordinates[0][0] < x < player1.coordinates[0][0]+20 and y+7 <player1.coordinates[0][1] <y+17:
        print ("oof")
        score+=1
        ateapple(score)
        x=random.randint(50,300)
        y=random.randint(50,300)
        player1.coordinates.insert(0,player1.coordinates[0])
    message_display(str(score),20,20)
    pygame.draw.rect(window,(0,255,0),(x,y,12,12))
    player1.draw()
    pygame.display.update()
    
    if player1.coordinates[0][0] <= 3 or player1.coordinates[0][0] >= 480 or player1.coordinates[0][1]<=3 or player1.coordinates[0][1]>=480:
        time.sleep(1)
        message_display('Game Over',250,20)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
