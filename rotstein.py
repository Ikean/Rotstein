import pygame, sys, os
from pygame.locals import *
import renderBackground
#from clickObj import clickObj
from execObj import Exec
import math
#import rotMngr

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,40)

pygame.init()
fpsClock = pygame.time.Clock()

class MasterMngr(object):
	def __init__(self):
		self.windowSurfaceObj = pygame.display.set_mode((1280,960),HWSURFACE|DOUBLEBUF) #|RESIZEABLE
		pygame.display.set_caption('Rotstein')

		self.mouseX, self.mouseY = 0, 0
		self.globalX, self.globalY = 0, 0
		self.middlePressed = False
		self.mmDistX, self.mmDistY = 0, 0
		self.leftPressed = False
		self.rightPressed = False

		self.whiteColor = pygame.Color(255, 255, 255)
		self.redColor = pygame.Color(255, 0, 0)
		self.brightGreyColor = pygame.Color(57, 57, 57)

		self.fontObj = pygame.font.Font('BebasNeue.otf', 21)

		self.bgRender = renderBackground.bgRenderer(self.windowSurfaceObj)

		self.rElements = []
		
		self.mouseTarget = None

		self.rElements.append(Exec(self))
		self.rElements.append(Exec(self))

		#statischen elemente wie knoepfe initisialisieren


	def update(self):		
		for ele in self.rElements:
			if(ele.update(self.globalX, self.globalY, self.mouseX, self.mouseY)):
				self.mouseTarget = ele
				return
		self.mouseTarget = None

	def renderFPS(self):
		fpsMsg = self.fontObj.render(str(fpsClock.get_fps())[0:5] + " FPS", True, self.redColor)
		self.windowSurfaceObj.blit(fpsMsg, (4,4))

		gCoordMsg = self.fontObj.render("gX: " + str(self.globalX) + " gY: " + str(self.globalY), True, self.redColor)
		self.windowSurfaceObj.blit(gCoordMsg, (4, 24))

		mCoordMsg = self.fontObj.render("mx: " + str(self.mouseX) + " my: " + str(self.mouseY), True,self. redColor)
		self.windowSurfaceObj.blit(mCoordMsg, (4, 48))

		pygame.draw.circle(self.windowSurfaceObj, self.whiteColor, (self.globalX, self.globalY) , 5, 0)

		pygame.display.update()

	def render(self):
		#hintergrund	
		self.bgRender.renderBackground(self.globalX, self.globalY)	
		#elemente
		for ele in reversed(self.rElements):
			ele.render(self.globalX, self.globalY)
		#std info

		self.renderFPS()
		pygame.display.update()

rot = MasterMngr()

while True:
	rot.update()
	rot.render()
	


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
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
				print("maus runter")
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

		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))

	fpsClock.tick(60)	
