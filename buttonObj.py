import pygame
import math
from pygame.locals import *

from clickObj import clickObj

class Button(object):
	"""docstring for Button"""
	def __init__(self,pMaster):
		self.img = pygame.image.load('assets/button.png')
		self.img = self.img.convert_alpha()
		super(Button, self).__init__(pMaster)
		
