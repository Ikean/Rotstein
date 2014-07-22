import pygame
import math
from pygame.locals import *

from clickObj import clickObj
from connectionObj import Connection

class Exec(clickObj):
	def __init__(self, pWindowSurfaceObject, pImg):
		super(Exec, self).__init__(pWindowSurfaceObject, pImg)
		connImg = pygame.image.load('assets/button.png')
		inConnection = Connection(pWindowSurfaceObject, connImg)
		inConnection.move(0, 100)		
		self.children.append(inConnection)

