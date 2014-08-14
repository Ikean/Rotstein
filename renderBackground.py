'''
@author: Hannez/Ikean
'''

import pygame
import math
from pygame.locals import *
		

class bgRenderer(object):
	def __init__(self, pWindowSurfaceObj):
		self.windowSurfaceObj = pWindowSurfaceObj
		self.bgImg = pygame.image.load('assets/bg.png')
		self.bgImg = self.bgImg.convert()

		self.bgih = self.bgImg.get_height()
		self.bgiw = self.bgImg.get_width()
		self.wsh = 0
		self.wsw = 0

		self.tileRepeat = 11
		
		self.x = 0 #-self.tileRepeat*self.bgiw/2
		self.y = 0 #-self.tileRepeat*self.bgih/2


		self.updateWindowSize()

		self.bg = pygame.Surface((self.bgiw*self.tileRepeat, self.bgih*self.tileRepeat))

		for w in range(self.tileRepeat):
			for h in range(self.tileRepeat):
				self.bg.blit(self.bgImg, (w*self.bgiw, h*self.bgih))

		self.bgh = self.bg.get_height()
		self.bgw = self.bg.get_width()

	def updateWindowSize(self):
		self.wsh = self.windowSurfaceObj.get_height()
		self.wsw = self.windowSurfaceObj.get_width()

	def renderBackground(self,pX,pY):
		if(self.x + pX > 0):
			#print("collision left")
			self.x-=self.bgiw
		elif(self.x + pX + self.bgw < self.wsw):
			#print("collision right")
			self.x+=self.bgiw
		if(self.y + pY > 0):
			#print("collision up")
			self.y-=self.bgih
		elif(self.y + pY + self.bgh < self.wsh):
			#print("collision down")
			self.y+=self.bgih

		self.windowSurfaceObj.blit(self.bg, (self.x + pX, self.y + pY))

		
		