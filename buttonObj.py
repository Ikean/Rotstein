import pygame
import math
from pygame.locals import *

from execObj import Exec
from clickObj import clickObj

class Button(clickObj):
	"""docstring for Button"""
	def __init__(self,pMaster):
		self.img = pygame.image.load('assets/button.png')
		self.img = self.img.convert_alpha()
		self.name = "button"
		self.imgp = pygame.image.load('assets/buttonPressed.png')
		self.imgp = self.imgp.convert_alpha()
		super(Button, self).__init__(pMaster)
		self.x = 300
		self.y = 10
		self.type = 'button'

	def move(self, x, y):
		pass
	
	def render(self, pGX, pGY):
		if(self.hover):
			#self.hoverBorder(pGX, pGY)
			self.wso.blit(self.imgp, (self.x, self.y))
		else:	
			self.wso.blit(self.img, (self.x, self.y))

	def click(self):
		ele = Exec(self.master)
		ele.x = -self.master.globalX+self.wso.get_width()/2-100
		ele.y = -self.master.globalY+self.wso.get_height()/2-100
		self.master.rElements.append(ele)

	def delete(self):
		pass #buttons cant be deleted

	def update(self, pGX, pGY, pMX, pMY): #figures out if mouse is hovering over it
		self.customUpdate()

		if(self.x < pMX and 
			self.x + self.collW > pMX and
			self.y < pMY and
			self.y + self.collH > pMY):
			self.hover = True
			return True
		else:
			self.hover = False
			return False