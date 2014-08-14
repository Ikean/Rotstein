'''
@author: Hannez/Ikean
'''
import pygame
from connectionObj import Connection

class CallObj(object):
    #reihenfolge von den einzelnen executables

    def __init__(self, pMaster):
        self.master = pMaster        
        self.wso = self.master.windowSurfaceObj
        self.wsow = self.wso.get_width()
        self.connections = []
        self.img = pygame.image.load('assets/connection.png')
        self.img = self.img.convert_alpha()
        newConnection = Connection(self.master, self, 0, 0)
        newConnection.type = "callConn"
        self.connections.append(newConnection)
        self.master.rElements.append(newConnection)
        self.iw = 0
        self.hover = False
    
    def addConn(self):
        height = len(self.connections)*46
        newImg = pygame.Surface((13, height), pygame.SRCALPHA, 16)
        newImg = newImg.convert_alpha()
        pygame.draw.line(newImg, (150, 150, 150), (5, 0), (5, height), 2)
        newImg.blit(self.img, (0,0))
        self.img = newImg
        newConnection = Connection(self.master, self, 0, height-13)
        newConnection.type = "callConn"
        self.connections.append(newConnection)
        self.master.rElements.append(newConnection)
        
    def update(self):
        if(self.connections[-1].connectedTo is not None):
            self.addConn()
        return False
    
    def hover(self):
        return False
    
    def clickEnd(self):
        return False
    
    def delete(self):
        pass
            
    def render(self, pGX, pGY):
        if (pGX + 13 < 0 or
             pGX + 13 > self.wsow):            
            return
        self.wso.blit(self.img, (pGX, pGY))
            
    def getX(self):
        return 0
    
    def getY(self):
        return 0