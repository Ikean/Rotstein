import pygame
import math
from pygame.locals import *

from clickObj import clickObj
from connectionObj import Connection

class Exec(clickObj):
	def __init__(self, pWindowSurfaceObject, pEleList):
		print("Exec erstellt")
		self.img = pygame.image.load('assets/cmd_.png')
		super(Exec, self).__init__(pWindowSurfaceObject, pEleList)
		self.collH = 36
		inConnection = Connection(pWindowSurfaceObject, pEleList)
		inConnection.parent = self
		self.rElements.append(inConnection)


