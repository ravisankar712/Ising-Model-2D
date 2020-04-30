import numpy as np
from p5 import *

width = 640
height = 640
res = 20
x = int(width/res)
y = int(height/res)
lattice = np.zeros((x, y))
for i in range(x):
		for j in range(y):
			if np.random.random() < 0.5:
				lattice[i, j] = 1
			else:
				lattice[i, j] = -1

J = 4.0 #nearest neighbours in 2D
beta = 10 #beta = 10 is the critical point
B = 0.0		#magnetic field

def show():
	for i in range(x):
		for j in range(y):
			if lattice[i, j] == 1:
				c = 0
			else:
				c = 255
			stroke(c)
			fill(c)
			rect((i * res, j * res), res, res)

def metropolis():
	i = np.random.randint(x)
	j = np.random.randint(y)

	if i != x-1 and j != y-1:
		NN_sum = (lattice[i + 1, j] + lattice[i - 1, j] + 
				  lattice[i, j + 1] + lattice[i, j - 1])
	elif i != x-1 and j == y-1:	
		NN_sum = (lattice[i + 1, j] + lattice[i - 1, j] + 
				  lattice[i, 0] + lattice[i, j - 1])
	elif i == x-1 and j != y-1:	
		NN_sum = (lattice[0, j] + lattice[i - 1, j] + 
				  lattice[i, j + 1] + lattice[i, j - 1])
	elif i == x-1 and j == y-1:	
		NN_sum = (lattice[0, j] + lattice[i - 1, j] + 
				  lattice[i, 0] + lattice[i, j - 1])

	E_ij = -J * lattice[i, j] * NN_sum - B * lattice[i, j]
	E_ij_F = -1 * E_ij
	if E_ij_F < E_ij:
		lattice[i, j] *= -1
	else:
		r = np.random.random()
		if r > np.exp(-beta * (E_ij_F - E_ij)):
			pass
		else:
			lattice[i, j] *= -1





def setup():
	size(width, height)

def draw():
	background(0)
	for i in range(500):
		metropolis()
	show()
	

run()