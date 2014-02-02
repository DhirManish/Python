#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.py
#  
#  Copyright 2014 Ajay Bhatia <ajay@dumb-box>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


#Catch the Ball by Xcmd
#
#A very simple game: just move the mouse and try to get the pointer over the ball.

#Import the good stuff! Read tutorials to find out why...
import sys, pygame, random
from pygame.locals import *

#Check if the fonts module loaded. If not, oosp.
if not pygame.font: print "Fonts disabled!"
pygame.init()
random.seed(pygame.time.get_ticks())

#Random numbers for some reason... hmm... what could r g b mean?
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

#Defining some stuff... size... speed... black?!
size = width, height = 800, 600
speed = [1, 1]
black = 0,0,0

#Setting up the screen the player sees. See how size comes from
#up there to down here? Nifty!
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Catch the Ball!")

#Yes, I literally made a .png of a ball...
#I'm using convert_alpha() because I want to use the PNG's
#transparency layer instead of defining one myself. This
#also helps speed things up as far as the game goes because
#the game doesn't have to keep converting the PNG file into
#a useable graphic format. .convert() does the same thing
#but does not include transparency.
ball = pygame.image.load('/home/ajay/Codes/py/ball.png').convert_alpha()

#Rects are your friends. Please read up on them.
ballrect = ball.get_rect()

#Hey, I remember r g b!
fontColor = r,g,b

#Oh honh honh! Zee font! She is Tres Arial!
font = pygame.font.SysFont("Arial Black", 25)

#winText is a surface... just in case you didn't know..
winText = font.render('You caught the ball! [Click to Play Again]', 0, fontColor)

#Look, another rect!
winRect = [0,0,0,0]

#Are we currently in a state where we've caught the ball?
caught = 0

#This is just because I wanted to show an updating surface that's
#a little more obvious than the ball zipping around.

#tix = ticks. How many ticks have passed since this was called?
tix = pygame.time.get_ticks()

#tixText = a surface!
tixText = font.render(str(tix), 0, fontColor)

#Hmm... another rect... why did I define it as nothing?
tixRect = [0,0,0,0]

#How many times did we catch the ball? Tell the user!
caughtAmt = 0
caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
caughtRect = [0,0,0,0]

#MAIN LOOP GO GO GO!
while 1:
	
	#Update the Tix! WOO!
	tix = pygame.time.get_ticks()
	tixText = font.render(str(tix), 0, fontColor)
	
	#Check some events. WICKED.
	for event in pygame.event.get():
		#QUITTERS QUIT, MEG!
		if event.type == pygame.QUIT:
			print "Quit event detected. Good bye!"
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			#DING FRIES ARE DONE.
			ding = event.pos
			
			#Did the mouse collide with the rect of the ball? THEN WE CAUGHT IT! YEY!
			if ballrect.collidepoint(ding) and caught != 1:
				caught = 1
				caughtAmt = caughtAmt + 1
				caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
		
		#Okay, so this only works when we caught the ball. If we click
		#the mouse, then we get to go again.
		if event.type == pygame.MOUSEBUTTONUP:
			if caught == 1 and event.button == 1:
				caught = 0
				speed[0] = speed[0] + 1
				speed[1] = speed[1] + 1
	
	#LIGHTNING SPEED GO! If the left-side of the ballrect is at or less
	#than the 0 position of the left-hand side of the screen OR it is
	#GREATER than or EQUAL TO the RIGHT HAND side of the screen...
	#then we need to change the direction. Same thing for top and bottom.
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	
	#fill the back of the screen with black
	screen.fill(black)
	
	#draw us a ball!
	screen.blit(ball, ballrect)
	
	#draw the surface caughtText in the upper-right
	caughtRect = screen.blit(caughtText, (600, 0))
	
	#draw the surface of the ticks counter in the upper-left
	tixRect = screen.blit(tixText, (0,0))
	
	#IF and ONLY IF we're currently in the "caught ball" state...
	#draw the winText. Oh, also prevent the ball from moving.
	if caught == 1:
		winRect = screen.blit(winText, (50, 350))
		speed = [0, 0]
	
	#What are we updating? Everything!
	updates = ballrect, tixRect, winRect, caughtRect
	pygame.display.update(updates)
