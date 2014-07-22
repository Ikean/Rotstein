import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Connection(clickObj):	
	def __init__(self, pWindowSurfaceObject):
		self.img = pygame.image.load('assets/connection.png')
		super(Connection, self).__init__(pWindowSurfaceObject)
		print("Connection erstellt")	
