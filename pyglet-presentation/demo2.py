

import pyglet
from pyglet.gl import *


class Window(pyglet.window.Window):

	def __init__(self):
		super(Window, self).__init__()
		vertices = [ 0, 0, 0,
		             0, 1, 0,
		             1, 0, 0 ]
		self.vertices = pyglet.graphics.vertex_list(3, ("v3f", vertices))


	def on_draw(self):

		glClearColor(0.53, 0.81, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(60, self.width / float(self.height), 0.1, 1000.0)
		gluLookAt(0, 0, 4, 	# Camera x, y, z
			      0, 0, 0, 	# Camera focus
			      0, 1, 0) 	# Up

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		self.vertices.draw(GL_TRIANGLES)

		return pyglet.event.EVENT_HANDLED



window = Window()
pyglet.app.run()

