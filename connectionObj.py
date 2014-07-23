import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Connection(clickObj):	
	def __init__(self, pMaster, parent):
		print("Connection erstellt")
		self.img = pygame.image.load('assets/connection.png')
		self.img = self.img.convert_alpha()
		super(Connection, self).__init__(pMaster)
		self.parent = parent		

		self.ax = 0 #additional x
		self.ay = 100

		self.parent.img.blit(self.img, (self.ax, self.ay))

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


	def drange(self, start, stop, step):
		r = start
		while r < stop:
			yield r
			r += step

	def drawBerzier(self):
		l = math.fabs((self.x + self.master.globalX + self.iw/2) - (self.master.mouseX))
		erster_x = self.x + self.master.globalX + self.iw/2
		erster_y = self.y + self.master.globalY + self.ih/2
		zweiter_x = self.x + self.master.globalX + self.iw/2 - l
		zweiter_y = self.y + self.master.globalY + self.ih/2
		dritter_x = self.master.mouseX + l
		dritter_y = self.master.mouseY
		vierter_x = self.master.mouseX
		vierter_y = self.master.mouseY

		letzter_x=erster_x
		letzter_y=erster_y
	
		for u in self.drange(0, 1, 0.05):
			posx=pow(u,3)*(vierter_x+3*(zweiter_x-dritter_x)-erster_x)+3*pow(u,2)*(erster_x-2*zweiter_x+dritter_x)+3*u*(zweiter_x-erster_x)+erster_x
			posy=pow(u,3)*(vierter_y+3*(zweiter_y-dritter_y)-erster_y)+3*pow(u,2)*(erster_y-2*zweiter_y+dritter_y)+3*u*(zweiter_y-erster_y)+erster_y
			pygame.draw.line(self.wso, (255, 255, 255), (letzter_x, letzter_y), (posx, posy))
			letzter_x=posx
			letzter_y=posy
			
		pygame.draw.line(self.wso, (0, 255, 255), (erster_x, erster_y), (zweiter_x, zweiter_y))
		pygame.draw.line(self.wso, (255, 255, 0), (dritter_x, dritter_y), (vierter_x, vierter_y))

	def render(self, pGX, pGY):
		if(self.creatingConn):
			self.drawBerzier()
		#self.wso.blit(self.img, (self.x + pGX, self.y + pGY))