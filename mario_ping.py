import pygame, sys, random
from pygame.locals import *
import math

pygame.init()

# Window setup
frmWindow = pygame.display.set_mode((1024,768))
fpsClock = pygame.time.Clock()
pygame.display.set_caption("Pong game in Mario World")

# Load commands for images and sounds
pMario = pygame.image.load('MarioBackFixed.jpg')
pTurtle = pygame.image.load('Lakitu.PNG')
sndBackgound = pygame.mixer.music.load('Super Mario.mp3')
pygame.mixer.music.play(-1) # Play the background sound
sndBounceWall = pygame.mixer.Sound('sndBallBounce.mp3')
pygame.mixer.music.set_volume(0.1) # Background sound volume
pygame.mixer.Sound.set_volume(sndBounceWall,0.2) # Ball bounce sound volume

# Background fill colour
clrBlack = (0,0,0)

#Ball Variables
BallXSpeed = 5 #Horizontal speed
BallYSpeed = 5 #Vertical speed
BallX = 100
BallY = 300
BallRadius = 35
BallColour = (134,1,175) #ice blue 

#Paddle Object Variables
PaddleXSpeed = 0 # Only moves horizontally
PaddleX = 100
PaddleY = 600
PaddleWidth = 150
PaddleThick = 20 
PaddleColour = (0,0,125)

#Lakitu(UFO) Position
LakituXSpeed = 5
LakituX = 100
LakituY = 100

# Lakitu shield
ShieldXSpeed = 5
ShieldX = 240
ShieldY = 215
ShieldRadius = 80
ShieldColor = (0,255,0)
LakituDistanceToOrb = 0

RunGame = True
while RunGame:
	for event in pygame.event.get():
		if event.type == QUIT:
			RunGame = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				PaddleXSpeed = -5
			if event.key == pygame.K_RIGHT:
				PaddleXSpeed = 5
	# Update the monitor
	frmWindow.fill(clrBlack)
	frmWindow.blit(pMario, (0,0))
	frmWindow.blit(pTurtle, (LakituX, LakituY))
	
	
	# Update Ball Position
	BallX += BallXSpeed
	BallY += BallYSpeed
	
	#Update Paddle Position
	PaddleX += PaddleXSpeed
	
	#Upadate Lakitu(UFO) Position
	LakituX += LakituXSpeed
	
	#Update Lakitu Shield Position
	ShieldX += ShieldXSpeed
	
	# Wall Collision Section
	if BallX > 1024 - BallRadius or BallX - BallRadius < 5:
		BallXSpeed *= -1
		sndBounceWall.play()

	if BallY > 768 - BallRadius or BallY - BallRadius < 5:
		BallYSpeed *= -1
		sndBounceWall.play()
		
	
	# Paddle Collision Section
	if PaddleX > 1024 - PaddleWidth or PaddleX < 5:
		PaddleXSpeed *= -1
		
	
	# Lakitu comes out from the other side 
	if LakituX > 1024 and ShieldX > 1024:
		LakituX = -200
		ShieldX = -60
	
	# Ball collision with paddle
	if BallY >= 566 and BallX > PaddleX - BallRadius and BallX < PaddleX + PaddleWidth + BallRadius:
		BallYSpeed *= -1
		sndBounceWall.play()
		
	LakituDistanceToOrb = math.sqrt((ShieldX - BallX)**2 + (ShieldY - BallY)**2)
	
	if LakituDistanceToOrb < BallRadius + ShieldRadius + 5:
		BallXSpeed *= -1
		BallYSpeed *= -1
		
		
	
	

	#Draw the board section
	#Paint screen draw ball
	pygame.draw.circle(frmWindow, BallColour, (BallX, BallY), BallRadius, 0)
	
	pygame.draw.rect(frmWindow, PaddleColour, (PaddleX, PaddleY, PaddleWidth, PaddleThick), 0)
	
	pygame.draw.circle(frmWindow, ShieldColor, (ShieldX, ShieldY), ShieldRadius, 3)
	
	pygame.display.update()
	fpsClock.tick(50)
