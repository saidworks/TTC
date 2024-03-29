from turtle import *
import random
xmax = 250
xmin = -250
ymax = 250
ymin = -250
proximity = 10
def sensor():
    if xmax - position()[0] < proximity:
    #Too close to right wall
        return True
    if position()[0] - xmin < proximity:
    #Too clsoe to left wall
        return True
    if ymax - position()[1] < proximity:
    #Too close to top wall
        return True
    if position()[1] - ymin < proximity:
    #Too clsoe to bottom wall
        return True
    #Not too close to any
    return False

def straightline():
    '''Move in a random direction until sensor is triggered'''
    #Pick a random direction
    left(random.randrange(0,360))
    #Keep going forward until a wall is hit
    while not sensor():
        forward(1)

def spiral(gap = 20):
    ''''Move in a spiral with spacing gap'''
    #Determine starting radius of spiral based on the gap
    current_radius = gap
    while not sensor():
    #Determine how much of the circumference 1 unit is
        circumference = 2 * 3.14159*current_radius
        fraction = 1/circumference
    #Move as if in a circle of that radius
        left(fraction*360)
        forward(1)
    #Change radius so that we will be out by 2*proximity after 360 degrees
        current_radius += gap*fraction

def followwall(min):
    '''Move turtle parallel to nearest wall for amount distance'''
    #find nearest wall and turn parallel to it
    min = xmax - position()[0]
    setheading(90)
    if position()[0] - xmin < min:
        min = position()[0] - xmin
        setheading(270)
    if ymax - position()[1] < min:
        min = ymax - position()[1]
        setheading(180)
    if position()[1] - ymin < min:
        setheading(0)
    #Keep going until hitting another wall
    while not sensor():
        forward (1)
def backupspiral(backup = 100, gap = 20):
    '''First move backward by amount backup, then in a spiral with spacing gap'''
    #first back up by backup amount
    while not sensor() and backup > 0:
        backward(1)
        backup -= 1
    #Determine starting radius of spiral based on the gap
    spiral(gap)
#run functions
speed(0)
#Start with a spiral
spiral(40)
while (True):
#First back up so no longer colliding
    backward(1)
#Pick one of the three behaviors at random
    which_function = random.choice(['a', 'b', 'c'])
    if which_function == 'a':
        straightline()
    if which_function == 'b':
        backupspiral(random.randrange(100,200), random.
        randrange(10,50))
    if which_function == 'c':
        followwall(random.randrange(100,300))