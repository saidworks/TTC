import turtle
said=turtle.Turtle()
said.pendown()
said.speed(1)
#define functions
def startPos():
    said.penup()
    startposition = said.pos()
    said.goto(startposition[0]-300, startposition[1]-50)
def shift_right():
    said.penup()
    said.forward(5)
    said.pendown()

def drawTally():
    said.pendown()
    said.left(90)
    said.forward(20)
    said.backward(20)
    said.right(90)
    shift_right()

def drawSlash():
    #move up
    said.left(90)
    said.penup()
    said.forward(3)
    said.pendown()

    #draw slash
    startposition=said.pos()
    said.goto(startposition[0]-25,startposition[1]+14)
    #return to starting position
    said.penup()
    said.goto(startposition)
    said.backward(3)
    said.right(90)
    said.pendown()
def drawFive():
    drawTally()
    drawTally()
    drawTally()
    drawTally()
    drawSlash()
    shift_right()
    shift_right()
def drawTallies(n):
    while(n>=5):
        drawFive()
        n = n-5
    while(n>=1):
        drawTally()
        n = n - 1
drawTallies(50)

# #call functions
# startPos()
# for i in range(50):
#     drawFive()