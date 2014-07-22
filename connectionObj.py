import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Connection(clickObj):	
	def __init__(self, pMaster):
		print("Connection erstellt")
		self.img = pygame.image.load('assets/connection.png')
		super(Connection, self).__init__(pMaster)

		self.ax = 0 #additional x
		self.ay = 100

		self.creatingConn = False

	def move(self, x, y):
		pass

	def customUpdate(self):
		self.x = self.parent.getX() + self.ax
		self.y = self.parent.getY() + self.ay

	def click(self):
		print("connection clicked")
		self.creatingConn = True

	def clickEnd(self):
		if(self.creatingConn):
			print("connection click end")
			self.creatingConn = False

	def render(self, pGX, pGY):
		if(self.creatingConn):
			pass
		self.wso.blit(self.img, (self.x + pGX, self.y + pGY))