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
        self.Lifetime = pygame.time.get_ticks() + (int(rnd.randint(6000, 7000))) # Random Number in Milliseconds
        self.Color = (70, 200, 70)  # Green Color
        self.Value = rnd.randint(97, 122)   # ASCII Integer
    def Update(self):
        if (3 > int(rnd.randint(0,100))):
            self.Value = rnd.randint(97, 122)

def AddCode():
    rndX = int(rnd.randint(0, GSizeX))
    rndY = int(rnd.randint(0, int(GSizeY / 2)))
    lenC = int(rnd.randint(10, 30))
    return OneCode(rndX, rndY, lenC)


SizeX = 1024
SizeY = 768

# Setup Graphics with pygame
pygame.init()
Screen = pygame.display.set_mode((SizeX, SizeY))
pyFont = pygame.font.Font(r"C:\DATA\Workspace\matrixcode\matrix code nfi.ttf", 20)
# Calculate size for a single Character
FSizeX, FSizeY = pyFont.size("W")
GSizeX = int(SizeX / FSizeX)
GSizeY = int(SizeY / FSizeY)

# Add Code
CodeList = []
for _ in range(int(GSizeX * 0.10)):
    CodeList.append(AddCode())

matrix_tick = pygame.time.get_ticks()
addcode_tick = pygame.time.get_ticks()

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
        curX = ac.PosX * FSizeX
        curY = ac.PosY * FSizeY
        curColor = (255, 255, 255)
        if (ac.Leader == False):
            curColor = ac.Color
        # Draw a filled black Rectangle at the Code Position
        pygame.draw.rect(Screen, (0, 0, 0), (curX, curY, FSizeX, FSizeY))
        # Draw the text Code
        ntxt = pyFont.render(chr(ac.Value), True, curColor)
        Screen.blit(ntxt, (curX, curY))

    # Switch current Screen to the Display
    pygame.display.flip()

    # Add more Code
    if (pygame.time.get_ticks() - addcode_tick) > 1000:
        # Calculate a Random Number for new Codes. Some Percent from the max X-Range
        newCodeCount = int(rnd.randint(1, int(GSizeX * 0.05)))
        print("Add New Code: ", newCodeCount)
        for _ in range(newCodeCount):
            CodeList.append(AddCode())
        addcode_tick = pygame.time.get_ticks()

    # If Tick has passed, update every Code
    if (pygame.time.get_ticks() - matrix_tick) > 150:
        matrix_tick = pygame.time.get_ticks()
        removeList = []
        appendList = []
        # Update every Code, create new Code, change Code settings
        for ac in CodeList:
            ac.Update()
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
