import pygame
import math
from pygame.locals import *

from clickObj import clickObj
from connectionObj import Connection

class Exec(clickObj):
	def __init__(self, pWindowSurfaceObject):
		self.img = pygame.image.load('assets/cmd_.png')
		super(Exec, self).__init__(pWindowSurfaceObject)
		self.collH = 36
		inConnection = Connection(pWindowSurfaceObject)
		inConnection.move(0, 100)		
		self.children.append(inConnection)

