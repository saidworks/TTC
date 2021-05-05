import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=400, height=300, caption='First Pyglet Window')
label_1 = pyglet.text.Label('Title', font_name='Times New Roman', font_size=16, x=150, y=250)
label_2 = pyglet.text.Label('Subtitle', font_name='Arial', font_size=14, x=150, y=200)
label_3 = pyglet.text.Label('Mouse Motion', font_name='Arial', font_size=14, x=150, y=150)


# event key pressed


# call back to functions
@window.event
def on_draw():
    window.clear()
    label_1.draw()  # display label
    label_2.draw()
    label_3.draw()


# keyboard events
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RETURN:
        key_pressed = 'Return'
    elif symbol == key.LEFT:
        key_pressed = 'Left arrow'
    else:
        key_pressed = 'unknown'
    global label_1
    label_1 = pyglet.text.Label(key_pressed, font_name='Arial', font_size=18, x=150, y=260)


# mouse events
@window.event
def on_mouse_press(x, y, button, modifiers):
    global label_2
    label_2 = pyglet.text.Label('Mouse click at position (' + str(x) + ',' + str(y) + ')',
                                font_name='Times New Roman', font_size=18, x=50, y=200)
@window.event
def on_mouse_motion(x, y, dx, dy):
    global label_3
    label_3 = pyglet.text.Label('Mouse click at position (' + str(x) + ',' + str(y) + ')',
                                font_name='Times New Roman', font_size=16, x=50, y=150)
#there is other events like on_mouse_release , on_mouse_drag
pyglet.app.run()
# Define functions to be used as callbacks

# Initialization:
# Set up any variables , data, etc.
# Register callbacks
# Start up event monitor
