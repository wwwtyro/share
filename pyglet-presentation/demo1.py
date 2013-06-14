
import pyglet
from pyglet.gl import *

class Window(pyglet.window.Window):

	def __init__(self):
		super(Window, self).__init__()

	def on_draw(self):
		glClearColor(0.53, 0.81, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT)
		return pyglet.event.EVENT_HANDLED

window = Window()
pyglet.app.run()

