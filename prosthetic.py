# Imported modules
import pygame
import pymunk
# Locally written modules
import body

# Constants
displayWidth = 500
displayHeight = 500

# Virtual simulation of prosthetic and environment
class VirtualSimulation:
    # Variables
    objects = []

    # Methods
    # Constructor
    def __init__(self):
        pygame.display.init()
        
    # Render simulation
    def renderSimulation(self):
        pygame.display.set_mode(size=(displayWidth, displayHeight), flags=0, depth=0, display=0, vsync=0)
        for obj in self.objects:
            drawObject(obj)
            
    # Draw object
    def drawObject(self):
        print("Body")

    # Create new object
    def createObject(self):
        print("Create")

virtualSimulation = VirtualSimulation()
virtualSimulation.renderSimulation()
