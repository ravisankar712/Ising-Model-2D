import numpy as np
from p5 import *
import pygame as pg 

pg.init()
pg.font.init() 
myfont = pg.font.SysFont('Comic Sans MS', 25)

width = 1000
height = 1000
res = 5
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
temp = 0.1
beta = 1/temp #beta = 10 is the critical point
B = 0.0		#magnetic field

def show():
	for i in range(x):
		for j in range(y):
			if lattice[i, j] == 1:
				c = (0, 0, 0)
			else:
				c = (255, 255, 255)
			pg.draw.rect(canvas, c, (int(i * res), int(j * res), res, res))

def metropolis(beta, B):
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


#drawing stuff
canvas = pg.display.set_mode((width, height))
clock = pg.time.Clock()

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			quit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP:
				temp += 0.05
			if event.key == pg.K_DOWN:
				if temp > 0.05:
					temp -= 0.05
			if event.key == pg.K_RIGHT:
				B += 0.1
			if event.key == pg.K_LEFT:
				B -= 0.1

	canvas.fill((0,0,0))
	for i in range(10000):
		metropolis(1/temp, B)
	show()
	textsurface1 = myfont.render('Temperature::' + str(temp), False, (255, 0, 0))
	canvas.blit(textsurface1, (0, 0))
	textsurface2 = myfont.render('Magnetic Field::' + str(B), False, (255, 0, 0))
	canvas.blit(textsurface2, (0, 50))
	
	pg.display.update()
	clock.tick(60)
