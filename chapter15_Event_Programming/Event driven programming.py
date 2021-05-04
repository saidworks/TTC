import pyglet
from pyglet.window import *



window = pyglet.window.Window(width=400,height=300,caption="TestWindow")
label = pyglet.text.Label('Nothing pressed so far',
                          font_name='Times New Roman',
                          font_size=18,
                          x=50,y=150)
img=pyglet.image.load('WIN_20200310_13_51_02_Pro.jpg')
imageWidth = 100
imageHeight = 100

img.width = imageWidth
img.height = imageHeight
@window.event
def on_key_press(symbol,modifiers):
    if symbol==key.LSHIFT or symbol==key.RSHIFT:
        key_pressed="shift"
    elif symbol==key.RETURN:
        key_pressed="return"
    elif symbol==key.NUM_1:
        key_pressed="number 1"
    else:
        key_pressed="unknown"
    global label
    label = pyglet.text.Label('You pressed the '+key_pressed+' key! ',
                              font_name='Times New Roman',
                              font_size=18,
                              x=50,y=150)
@window.event
def on_mouse_press(x,y,dx,dy):
    global label
    label = pyglet.text.Label('Mouse click at position('+str(x)+','+str(y)+')',
                              font_name='Times New Roman',
                              font_size=18,
                              x = 50,y = 150)
@window.event
def on_draw():
    window.clear()
    label.draw()
    img.blit(100,100)

pyglet.app.run()
#Define functions to be used as callbacks

#Initialization:
    #Set up any variables , data, etc.
    #Register callbacks
    #Start up event monitor