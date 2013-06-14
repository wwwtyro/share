

import pyglet
from pyglet.gl import *
import art


class Window(pyglet.window.Window):

	def __init__(self):
		super(Window, self).__init__()

		vertices = []
		colors = []
		terrainSize = 64
		for x in range(-terrainSize,terrainSize):
			for z in range(-terrainSize,terrainSize):
				y0 = art.heightMap(x + 0, z + 0)
				y1 = art.heightMap(x + 0, z + 1)
				y2 = art.heightMap(x + 1, z + 0)
				y3 = art.heightMap(x + 1, z + 1)
				vertices += (x+0, y0, z+0)
				vertices += (x+0, y1, z+1)
				vertices += (x+1, y2, z+0)
				vertices += (x+1, y2, z+0)
				vertices += (x+0, y1, z+1)
				vertices += (x+1, y3, z+1)
				c0 = art.color(x + 0, z + 0, y0)
				c1 = art.color(x + 0, z + 1, y1)
				c2 = art.color(x + 1, z + 0, y2)
				c3 = art.color(x + 1, z + 1, y3)
				colors += c0
				colors += c1
				colors += c2
				colors += c2
				colors += c1
				colors += c3
		self.vertices = pyglet.graphics.vertex_list(terrainSize**2 * 24, ('v3f', vertices), ('c3f', colors))

		# Schedule animation.
		self.tick = 0
		pyglet.clock.schedule(self.update)



	def on_draw(self):

		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)

		glClearColor(0.53, 0.81, 1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(60, self.width / float(self.height), 0.1, 1000.0)
		gluLookAt(0, 38, 64, 	# Camera x, y, z
			      0,  0,  0, 	# Camera focus
			      0,  1,  0)  	# Up

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glRotatef(self.tick*0.125, 0.0, 1.0, 0.0)

		self.vertices.draw(GL_TRIANGLES)

		return pyglet.event.EVENT_HANDLED



	def update(self, dt):
		self.tick += 1
		return pyglet.event.EVENT_HANDLED



window = Window()
pyglet.app.run()

