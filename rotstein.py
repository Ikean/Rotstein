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

windowSurfaceObj = pygame.display.set_mode((1280,960),HWSURFACE|DOUBLEBUF) #|RESIZEABLE
pygame.display.set_caption('Rotstein')

mouseX, mouseY = 0, 0
globalX, globalY = 0, 0
middlePressed = False
mmDistX, mmDistY = 0, 0
leftPressed = False
rightPressed = False

whiteColor = pygame.Color(255, 255, 255)
redColor = pygame.Color(255, 0, 0)
brightGreyColor = pygame.Color(57, 57, 57)

fontObj = pygame.font.Font('BebasNeue.otf', 21)

bgRender = renderBackground.bgRenderer(windowSurfaceObj)

rElements = []

global mouseTarget
mouseTarget = None

rElements.append(Exec(windowSurfaceObj, rElements))

#statischen elemente wie knoepfe initisialisieren


def update():
	global mouseTarget
	for ele in rElements:
		if(ele.update(globalX, globalY, mouseX, mouseY)):
			mouseTarget = ele
			return
	mouseTarget = None

def renderFPS():
	fpsMsg = fontObj.render(str(fpsClock.get_fps())[0:5] + " FPS", True, redColor)
	windowSurfaceObj.blit(fpsMsg, (4,4))

	gCoordMsg = fontObj.render("gX: " + str(globalX) + " gY: " + str(globalY), True, redColor)
	windowSurfaceObj.blit(gCoordMsg, (4, 24))

	mCoordMsg = fontObj.render("mx: " + str(mouseX) + " my: " + str(mouseY), True, redColor)
	windowSurfaceObj.blit(mCoordMsg, (4, 48))

	pygame.draw.circle(windowSurfaceObj, whiteColor, (globalX, globalY) , 5, 0)

	pygame.display.update()

def render():
	#hintergrund	
	bgRender.renderBackground(globalX, globalY)	
	#elemente
	for ele in reversed(rElements):
		ele.render(globalX, globalY)
	#std info

	renderFPS()
	pygame.display.update()


while True:
	update()
	render()
	


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouseX, mouseY = event.pos			
			if(middlePressed):
				globalX = mouseX - mmDistX
				globalY = mouseY - mmDistY
			if(leftPressed):
				if(mouseTarget):
					mouseTarget.move(mouseX - mmDistX, mouseY - mmDistY)

		elif event.type == MOUSEBUTTONDOWN: #maus runter
			mouseX, mouseY = event.pos
			if event.button == 2:
				pygame.mouse.set_cursor(*pygame.cursors.diamond)
				middlePressed = True
				mmDistX = mouseX - globalX
				mmDistY = mouseY - globalY
			elif event.button == 1:
				if(mouseTarget):
					mmDistX = mouseX - mouseTarget.getX()
					mmDistY = mouseY - mouseTarget.getY()
					mouseTarget.click()
					leftPressed = True

		elif event.type == MOUSEBUTTONUP: #maus hoch
			mouseX, mouseY = event.pos
			if event.button == 2:
				pygame.mouse.set_cursor(*pygame.cursors.arrow)
				middlePressed = False
			elif event.button == 1:
				leftPressed = False
				for ele in rElements:
					ele.clickEnd()
			elif event.button == 2:
				rightPressed = False
			elif event.button == 3:
				print(rElements)

		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))

	fpsClock.tick(60)	
