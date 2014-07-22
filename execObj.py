import pygame
import math
from pygame.locals import *

from clickObj import clickObj
from connectionObj import Connection

class Exec(clickObj):
	def __init__(self, pMaster):
		print("Exec erstellt")
		self.name = "Exec"
		self.img = pygame.image.load('assets/cmd_.png')
		super(Exec, self).__init__(pMaster)
		self.collH = 36
		inConnection = Connection(pMaster)
		inConnection.parent = self
		inConnection.name = "inputExec"
		self.rElements.append(inConnection)


