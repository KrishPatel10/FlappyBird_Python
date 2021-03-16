#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pygame
import sys
import random

pygame.init()

width = 1270
height = 720
screen = pygame.display.set_mode((width,height))

#image load

bg = pygame.image.load("sprites/BG.png")
bird = pygame.image.load("sprites/bird.png")
pipeup = pygame.image.load("sprites/pipeupi.png")
pipedown = pygame.image.load("sprites/pipedowni.png")
point = pygame.mixer.Sound("audio/point.wav")
hit = pygame.mixer.Sound("audio/hit.wav")


# In[33]:


class game:
    def __init__(self):
        self.Gameon = True
        self.BirdX = 100
        self.BirdY = 100
        self.gravity = 0
        self.pipevel = 0
        self.flap = 0
        self.score = 0
        self.Key = False
        self.gameover = False
        self.playsound = True
        self.pipeX = [width,width+200,width+400,width+600,width+800,width+1000,width+1200]
        self.pipeupi = [self.pipeup(),self.pipeup(),self.pipeup(),self.pipeup(),self.pipeup(),self.pipeup(),self.pipeup()]
        self.pipedowni = [self.pipedown(),self.pipedown(),self.pipedown(),self.pipedown(),self.pipedown(),self.pipedown(),self.pipedown()]
        
    def pipeup(self):
        return random.randrange(int(height/2)+50,int(height)-20)
        
    def pipedown(self):
        return random.randrange(-int(height/2)+100,-100)
    
    def flapping(self):
        if(self.gameover == False):
            self.flap -= 1
            self.BirdY -= self.flap
            
    def text(self, text, color, x, y, size, style, bold=False):
        font = pygame.font.SysFont(style, size, bold=bold)
        screen_txt = font.render(text, True, color)
        screen.blit(screen_txt, (x,y))
            
    def movepipe(self):
        for i in range(0,7):
            self.pipeX[i] += -int(self.pipevel)
            
        for i in range(0,7):
            if(self.pipeX[i] <= -50):
                self.pipeX[i] = width+100
                self.pipeupi[i] = self.pipeup()
                self.pipedowni[i] = self.pipedown()
                
    def collide(self):
        for i in range(0,7):
            if((self.BirdX>=self.pipeX[i] and self.BirdX<(self.pipeX[i]+pipeup.get_width()))and(((self.BirdY+bird.get_height()-15)>=self.pipeupi[i]) or (self.BirdY<=self.pipedowni[i]+pipedown.get_height()-15))):
                return True
            
            elif(self.BirdX == self.pipeX[i] and (self.BirdY >= self.pipedowni[i] and self.BirdY<= self.pipeupi[i])):
                if(self.gameover==False):
                    self.score += 1
                    pygame.mixer.Sound.play(point)
            
            if self.BirdY <= 0:
                return True
            
            if ((self.BirdY+bird.get_height())>=height):
                self.gravity = 0
                return True
            
    def isgameover(self):
        if(self.collide()):
            self.gameover = True
            self.text("Game Over!", (255,255,0), 450, 300, 84, 'Fixedsys', bold = True)
            self.text("Press Enter to continue!", (255,255,0), 400, 600, 48, 'Fixedsys', bold = True)
            self.pipevel = 0
            self.flap = 0
            self.rotate = -90
            if(self.playsound):
                pygame.mixer.Sound.play(hit)
                self.playsound = False
        
    def MainGame(self):
        while self.Gameon:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if(self.gameover):
                            self.pipevel = 0
                        else:
                            self.pipevel = 1.5
                            
                        self.flap = 30
                        self.Key = True
                        self.isgameover()
                        self.flapping()
                        
                    if event.key == pygame.K_RETURN:
                        newgame = game()
                        newgame.MainGame()
                        
            if (self.Key==True):
                self.BirdY += 0.4
                
            if(self.collide()):
                self.BirdY += 1
                    
                    
            screen.blit(bg,(0,0))
            screen.blit(bird,(self.BirdX,self.BirdY))
            
            for i in range(0,7):
                screen.blit(pipeup,(self.pipeX[i],self.pipeupi[i]))
                screen.blit(pipedown,(self.pipeX[i],self.pipedowni[i]))
                
            
                
            self.isgameover()                
            self.movepipe()
            
            self.text(str(self.score), (255,255,0), 50, 50, 40, 'Fixedsys', bold = True)            
            
            pygame.display.update()
                    
    pygame.display.set_caption("Flappy Bird")
                    
flappybird = game()
flappybird.MainGame()


# In[ ]:





# In[ ]:




