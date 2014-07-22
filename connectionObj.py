import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Connection(clickObj):	
	def __init__(self, pWindowSurfaceObject, pImg):
		super(Connection, self).__init__(pWindowSurfaceObject, pImg)
		print("Connection erstellt")	
