import pygame
import math
from pygame.locals import *

from clickObj import clickObj
from connectionObj import Connection

class Exec(clickObj):
	def __init__(self, pMaster):
		print("Exec erstellt")
		self.img = pygame.image.load('assets/cmd_.png')
		self.img = self.img.convert_alpha()
		self.name = "Exec" + str(pygame.time.get_ticks())
		title = "Execuetable Cmd Blk"
		titleImg = pMaster.fontObj.render(title, False, pMaster.whiteColor)
		self.img.blit(titleImg, (50,7))
		super(Exec, self).__init__(pMaster)
		self.collH = 36
		inConnection = Connection(pMaster, self, 0, 100)		
		inConnection.name = "inputExec"
		inConnection.type = 'in'
		self.rElements.append(inConnection)

		outConnection = Connection(pMaster, self, 235, 100)		
		outConnection.name = "outputExec"
		outConnection.type = 'out'
		self.rElements.append(outConnection)

	def renderModeFaster(self):
		self.img = pygame.image.load('assets/cmd_.png')
		self.img = self.img.convert()