import random as rnd
import time
import pygame

# Description of the Code
# --------------------------
# * a Block Starts in the top third of the Screen at a Random Position
# * a Block Ends at a random Length
# * the Block extends with additional Characters at the lower end
# * the last Character is highlighted in a different Color (white)
# * a Block disappears after a short time
class OneCode:
    def __init__(self, PositionX, PositionY, LengthY):
        self.PosX = PositionX
        self.PosY = PositionY
        self.EndY = self.PosY + LengthY
        self.Leader = True
        self.Lifetime = pygame.time.get_ticks() + (int(rnd.randint(6000, 7000)))
        print(self.Lifetime)
        print(pygame.time.get_ticks())
        self.Color = (70, 200, 70)
        self.Value = rnd.randint(65, 125)

SizeX = 400
SizeY = 300

pygame.init()
Screen = pygame.display.set_mode((SizeX, SizeY))
pyFont = pygame.font.SysFont("Calibri", 12)

CodeList = []
CodeList.append(OneCode(5, 2, 20))

matrix_tick = pygame.time.get_ticks()

mainloop = True
while mainloop:

    # Listen for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    # Fill Screen with Single Color (Black)
    Screen.fill((0, 0, 0))

    # Loop through every Code and Draw it on the Screen
    for ac in CodeList:
        curX = ac.PosX * 12
        curY = ac.PosY * 12
        curColor = (255, 255, 255)
        if (ac.Leader == False):
            curColor = ac.Color
        ntxt = pyFont.render(chr(ac.Value), True, curColor)
        Screen.blit(ntxt, (curX, curY))

    # Switch current Screen to the Display
    pygame.display.flip()

    # If Tick has passed, update every Code
    if (pygame.time.get_ticks() - matrix_tick) > 250:
        matrix_tick = pygame.time.get_ticks()
        removeList = []
        appendList = []
        # Update every Code, create new Code, change Code settings
        for ac in CodeList:
            if (ac.PosY != ac.EndY):
                if (ac.Leader == True):
                    nc = OneCode(ac.PosX, ac.PosY + 1, ac.EndY - ac.PosY - 1)
                    appendList.append(nc)
                    ac.Leader = False
            else:
                ac.Leader = False
            if (pygame.time.get_ticks() > ac.Lifetime):
                removeList.append(ac)
        # Remove Code which has End Of Lifetime
        for rc in removeList:
            CodeList.remove(rc)
        # Add new Code
        for ac in appendList:
            CodeList.append(ac)
