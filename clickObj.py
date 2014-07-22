import pygame
import math
from pygame.locals import *

class clickObj(object):	
	def __init__(self, pWindowSurfaceObject, pImg):
		self.wso = pWindowSurfaceObject
		self.hover = False
		self.x = 0
		self.y = 0
		self.img = pImg
		self.ih = self.img.get_height()
		self.iw = self.img.get_width()
		self.orangeColor = pygame.Color(225, 102, 0)
		self.children = []
		self.doHover = True

	def render(self, pGX, pGY):
		if(self.hover and self.doHover):
			self.hoverBorder(pGX, pGY)
		self.wso.blit(self.img, (self.x + pGX, self.y + pGY))
		for child in self.children:
			child.render(pGX, pGY)
	def hoverBorder(self, pGX, pGY):
		a = self.x + pGX
		b = self.y + pGY-5
		c = self.x + pGX + self.iw
		d = self.y + pGY + self.ih 
		pygame.draw.line(self.wso, self.orangeColor, (a,b), (a,d), 3)
		pygame.draw.line(self.wso, self.orangeColor, (a,d), (c,d), 3)
		pygame.draw.line(self.wso, self.orangeColor, (c,d), (c,b), 3)
		pygame.draw.line(self.wso, self.orangeColor, (a,b), (c,b), 3)
	def move(self, x, y):
		for child in self.children:
			child.relMove(x-self.x, y-self.y)
		self.x = x
		self.y = y
	def relMove(self, x, y): #to move children
		self.x += x
		self.y += y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def click(self):
		pass
	def logicUpdate(self): #animations or for child-parent realtionships
		pass
	def checkForHover(self, pGX, pGY, pMX, pMY):
		if(pGX + self.x < pMX and 
			pGX + self.x + self.iw > pMX and
			pGY + self.y < pMY and
			pGY + self.y + self.ih > pMY):
			self.hover = True
			return True
		else:
			self.hover = False
			return False
		