import pygame, sys, os
from pygame.locals import *
import renderBackground
from copy import deepcopy
from execObj import Exec
from buttonObj import Button
from callObj import CallObj
import math
#import rotMngr

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,40)

pygame.init()
fpsClock = pygame.time.Clock()

class MasterMngr(object):
	def __init__(self):
		self.windowSurfaceObj = pygame.display.set_mode((1280,960),HWSURFACE|DOUBLEBUF) #|RESIZEABLE
		pygame.display.set_caption('Rotstein - by Ikean <nelion2@web.de>')

		self.mouseX, self.mouseY = 0, 0
		self.globalX, self.globalY = 200, 100
		self.middlePressed = False
		self.mmDistX, self.mmDistY = 0, 0
		self.leftPressed = False
		self.rightPressed = False
		self.slowMode = False
		self.__recoverStates = []

		self.whiteColor = pygame.Color(255, 255, 255)
		self.redColor = pygame.Color(255, 0, 0)
		self.brightGreyColor = pygame.Color(57, 57, 57)

		self.fontObj = pygame.font.Font('BebasNeue.otf', 21)
		
		self.rElements = []

		self.bgRender = renderBackground.bgRenderer(self.windowSurfaceObj)
		self.caller = CallObj(self)
		
		self.mouseTarget = None

		self.addDrei = fpsClock.get_fps()/30.0
		self.dreiF = 0

		#statischen elemente wie knoepfe initisialisieren
		self.rElements.append(Button(self))


	def update(self):

		for ele in self.rElements:
			if(ele.update(self.globalX, self.globalY, self.mouseX, self.mouseY)):
				if(not self.leftPressed):
					self.mouseTarget = ele
					return
		if(not self.leftPressed):
			self.mouseTarget = None
			
		self.caller.update()

		# if(self.slowMode == False):
		# 	if(fpsClock.get_fps() < 24.0):
		# 		if(pygame.time.get_ticks() > 3000):
		# 			self.slowMode = True
		# 			self.renderModeFaster()

	def createRecover(self): #for ctrl+z (undo)
		self.__recoverStates.append(deepcopy(self.rElements))

	def undo(self):
		self.rElements = self.__recoverStates.pop(-1)

	def renderFPS(self):
		fpsMsg = self.fontObj.render(str(fpsClock.get_fps())[0:5] + " FPS", True, self.redColor)
		self.windowSurfaceObj.blit(fpsMsg, (4,4))

		gCoordMsg = self.fontObj.render("gX: " + str(self.globalX) + " gY: " + str(self.globalY), True, self.redColor)
		self.windowSurfaceObj.blit(gCoordMsg, (4, 24))

		mCoordMsg = self.fontObj.render("mx: " + str(self.mouseX) + " my: " + str(self.mouseY), True,self. redColor)
		self.windowSurfaceObj.blit(mCoordMsg, (4, 48))


		pygame.display.update()

	def render(self):
		#hintergrund	
		self.bgRender.renderBackground(self.globalX, self.globalY)
		self.caller.render(self.globalX, self.globalY)
		#self.windowSurfaceObj.fill(self.whiteColor)
		#elemente
		for ele in reversed(self.rElements):
			ele.render(self.globalX, self.globalY)
		#std info

		self.renderFPS()
		pygame.display.update()

	def renderModeFaster(self):
		for obj in self.rElements:
			obj.renderModeFaster()

rot = MasterMngr()

while True:
	


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			rot.update()
			rot.render()
			rot.mouseX, rot.mouseY = event.pos			
			if(rot.middlePressed):
				rot.globalX = rot.mouseX - rot.mmDistX
				rot.globalY = rot.mouseY - rot.mmDistY
			if(rot.leftPressed):
				if(rot.mouseTarget):
					rot.mouseTarget.move(rot.mouseX - rot.mmDistX, rot.mouseY - rot.mmDistY)

		elif event.type == MOUSEBUTTONDOWN: #maus runter
			rot.mouseX, rot.mouseY = event.pos
			if event.button == 2:
				pygame.mouse.set_cursor(*pygame.cursors.diamond)
				rot.middlePressed = True
				rot.mmDistX = rot.mouseX - rot.globalX
				rot.mmDistY = rot.mouseY - rot.globalY
			elif event.button == 1:
				if(rot.mouseTarget):
					rot.mmDistX = rot.mouseX - rot.mouseTarget.getX()
					rot.mmDistY = rot.mouseY - rot.mouseTarget.getY()
					rot.mouseTarget.click()
					rot.leftPressed = True

		elif event.type == MOUSEBUTTONUP: #maus hoch
			rot.mouseX, rot.mouseY = event.pos
			if event.button == 2:
				pygame.mouse.set_cursor(*pygame.cursors.arrow)
				rot.middlePressed = False
			elif event.button == 1:
				rot.leftPressed = False
				for ele in rot.rElements:
					ele.clickEnd()
			elif event.button == 2:
				rot.rightPressed = False
			elif event.button == 3:
				print(rot.rElements)
				print(sys.getsizeof(rot.rElements))
				print(fpsClock.get_fps())

		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			elif event.key == K_x:
				for ele in rot.rElements:
					ele.delete()

	fpsClock.tick()	
