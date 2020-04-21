import turtle
cycle=int(input("How many cycle do you want?"))
said=turtle.Turtle()
said.speed(10)
said.penup()
said.backward(350)
#draw horizontal lines
def vertical(cycle,angle=90,go=10,distance=100):
        for i in range(cycle):
                said.pendown()
                said.right(angle)
                said.forward(distance)
                said.penup()
                said.left(angle)
                said.forward(go)
                said.pendown()
                said.left(angle)
                said.forward(distance)
                said.penup()
                said.right(angle)
                said.forward(go)
def draw_tally(cycle):
        for j in range(cycle):
                vertical(4)
                said.penup()
                said.left(0)
                said.forward(50)
draw_tally(cycle)