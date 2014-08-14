'''
@author: Hannez/Ikean
'''

import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Connection(clickObj):	
	def __init__(self, pMaster, parent, ax, ay):
		print("Connection erstellt")
		self.img = pygame.image.load('assets/connection.png')
		self.img = self.img.convert_alpha()
		super(Connection, self).__init__(pMaster)
		self.parent = parent
		self.hoverImg = pygame.image.load('assets/connectionHover.png')
		self.hoverImg = self.hoverImg.convert_alpha()
		self.type = 'connIn'
		self.ax = ax
		self.ay = ay 

		self.parent.img.blit(self.img, (self.ax, self.ay))

		self.creatingConn = False
		self.connectedTo = None
		self.renderConnection = True #when connecting connections both want to render the berzier, this prevents it

	def move(self, x, y):
		pass
	

	def customUpdate(self):
		self.x = self.parent.getX() + self.ax
		self.y = self.parent.getY() + self.ay
		

	def click(self):
		print("connection clicked")
		if(self.connectedTo):
			self.connectedTo.creatingConn = True
			self.connectedTo.renderConnection = True
			self.connectedTo.connectedTo = None
			self.connectedTo = None
			self.renderConnection = True			
		else:
			self.creatingConn = True

	def clickEnd(self):
		if(self.creatingConn):
			print("connection click end")
			self.creatingConn = False
			for ele in self.master.rElements:
				if(ele.hover): #must hover over it
					if(ele.parent != self.parent): #cant connect to own in/outs				
						if(ele.type == 'connIn' or ele.type == 'connOut' or ele.type == 'callConn'): #cant connect to none connection objects
							if(ele.type != self.type): #cant connect input to output or vice versa
								print(ele.type)
								if(ele.connectedTo is not None):
									ele.connectedTo.renderConnection=True
									ele.connectedTo.connectedTo = None #disconnect from myself
								self.connectedTo = ele
								ele.connectedTo = self
								ele.renderConnection = False


	def drange(self, start, stop, step):
		r = start
		while r < stop:
			yield r
			r += step

	def drawBerzier(self, tx, ty):
		l = math.fabs((self.x + self.master.globalX + self.iw/2) - (tx))
		erster_x = self.x + self.master.globalX + self.iw/2
		if(erster_x > self.parent.getX() + self.master.globalX + self.parent.iw/2):
			l = -l
		erster_y = self.y + self.master.globalY + self.ih/2
		zweiter_x = self.x + self.master.globalX + self.iw/2 - l
		zweiter_y = self.y + self.master.globalY + self.ih/2
		dritter_x = tx + l
		dritter_y = ty
		vierter_x = tx
		vierter_y = ty

		letzter_x=erster_x
		letzter_y=erster_y
	
		for u in self.drange(0, 1.01, 0.01):
			posx=pow(u,3)*(vierter_x+3*(zweiter_x-dritter_x)-erster_x)+3*pow(u,2)*(erster_x-2*zweiter_x+dritter_x)+3*u*(zweiter_x-erster_x)+erster_x
			posy=pow(u,3)*(vierter_y+3*(zweiter_y-dritter_y)-erster_y)+3*pow(u,2)*(erster_y-2*zweiter_y+dritter_y)+3*u*(zweiter_y-erster_y)+erster_y
			pygame.draw.line(self.wso, (255, 255, 255), (letzter_x, letzter_y), (posx, posy), 2)
			letzter_x=posx
			letzter_y=posy
			
		#pygame.draw.line(self.wso, (0, 255, 255), (erster_x, erster_y), (zweiter_x, zweiter_y))
		#pygame.draw.line(self.wso, (255, 255, 0), (dritter_x, dritter_y), (vierter_x, vierter_y))

	def render(self, pGX, pGY):
		if(self.creatingConn):
			self.drawBerzier(self.master.mouseX, self.master.mouseY)
		if(self.hover):
			self.wso.blit(self.hoverImg, (self.x + pGX, self.y + pGY))
		if(self.connectedTo and self.renderConnection):
			self.drawBerzier(self.connectedTo.x+6+pGX, self.connectedTo.y+6+pGY)
