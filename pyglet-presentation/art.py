
import perlin

perlin2 = perlin.Perlin2()


class RGBInterpolator:
    def __init__(self):
        self.points = []
    def add(self, x, r,g,b):
        self.points.append([x,(r,g,b)])
        self.sort()
    def sort(self):
        self.points.sort(key=lambda p: p[0])
    def interp(self, x):
        right = 0
        while self.points[right][0] < x:
            right+=1
            if right >= len(self.points):
                return self.points[-1][1]
        left = right - 1
        if left < 0:
            return self.points[0][1]
        idist = 1/(self.points[right][0] - self.points[left][0])
        d = x - self.points[left][0]
        s = (self.points[right][1][0]-self.points[left][1][0]) * idist
        r = self.points[left][1][0] + s * d
        s = (self.points[right][1][1]-self.points[left][1][1]) * idist
        g = self.points[left][1][1] + s * d
        s = (self.points[right][1][2]-self.points[left][1][2]) * idist
        b = self.points[left][1][2] + s * d
        return r,g,b

heightcolor = RGBInterpolator()
heightcolor.add(  0.00, 0.00, 0.00, 0.30)     # deep blue
heightcolor.add(  2.00, 0.00, 0.00, 0.80)     # blue
heightcolor.add(  4.00, 0.00, 0.80, 0.80)     # light blue
heightcolor.add(  6.00, 0.93, 0.84, 0.68)     # beach sand
heightcolor.add( 10.00, 0.47, 0.28, 0.00)     # dirt
heightcolor.add( 13.00, 0.00, 0.30, 0.00)     # grass
heightcolor.add( 20.00, 0.40, 0.40, 0.40)     # rock
heightcolor.add( 30.00, 1.00, 1.00, 1.00)     # snow

def color(x, y, height):
	c = octave(3, 1, x, y) * 0.1 + 0.9
	r,g,b = heightcolor.interp(height * c)
	return r,g,b

def octave(o, h, x, y):
	return perlin2.noise(x/float(o), y/float(o)) * h

def heightMap(x, y):
	h = octave(64, 32, x, y)
	h += octave(16, 4, x, y)
	h += octave(4, 1, x, y)
	return h

