import numpy as np
import random as rnd
import time

class OneCode:

    def __init__(self, px, py):
        self.posx = px
        self.posy = py
        self.maxlength = rnd.randint(5, 10)
        self.codeblock = []
        self.reached_end = False

    def extend_code(self):
        if (len(self.codeblock) < self.maxlength):
            if (len(self.codeblock) > 0):
                rInt = rnd.randint(0, 52) + 65
                self.codeblock[len(self.codeblock) - 1] = rInt
            self.codeblock.append(35)
        else:
            self.reached_end = True

    def get_code(self):
        return self.codeblock

def display_matrix(someMatrix):
    s = ""
    for linefill in range(sizeX):
        s += "*"
    print(s)
    for x in range(0, someMatrix.shape[0]):
        line = ""
        for y in range(0, someMatrix.shape[1]):
            line = line + chr(someMatrix[x][y])
        print('*' + line + '*')
    print(s)

def add_code_block():
    rndX = rnd.randint(0, sizeX - 1)
    rndY = int(rnd.randint(0, sizeY - 1) / 2)
    aCode = OneCode(rndX, rndY)
    print("Create Random Code: " + str(rndX) + " / " + str(rndY), " -> ", aCode.maxlength)
    codeList.append(aCode)


sizeX = 60
sizeY = 20
# Create 2d Array filled with Int-Value 32 (32 = ASCII Space)
matrix = np.full((sizeY, sizeX), 32, dtype=int)
codeList = []

print("Create Random Code Blocks")
for numblocks in range(5):
    add_code_block()

print("Start Raining Code")
addnew = 5
loops = 0
while loops < 80:
    loops += 1

    # --------------------------------
    # Add new CodeBlocks every 5 Loops
    if addnew == 0:
        addnew = 5
        for numblocks in range(5):
            add_code_block()
    else:
        addnew -= 1

    # ------------------------
    # Calculate new CodeBlocks
    print("calculate blocks")
    blockids = []
    for codeIndex in range(len(codeList)):
        codeList[codeIndex].extend_code()
        if codeList[codeIndex].reached_end == True:
            print("Delete CodeBlock: ", codeIndex)
            blockids.append(codeIndex)

    # ----------------------
    # Delete finished Blocks
    diff = 0
    for bid in blockids:
        codeList.pop(bid - diff)
        diff += 1

    # ------------------------------
    # Refresh Matrix with CodeBlocks
    print("refresh matrix")
    for codeIndex in range(len(codeList)):
        curCode = codeList[codeIndex]
        for codeY in range(len(curCode.codeblock)):
            matrix[curCode.posy + codeY, curCode.posx] = curCode.codeblock[codeY]

    # ----------------------
    # Display current Matrix
    display_matrix(matrix)
    time.sleep(0.25)


