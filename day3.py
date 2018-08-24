import math

n = 368078

sq = math.ceil(math.sqrt(n)) + 2
cx = int(math.ceil(sq/2)-1)
cy = int(math.ceil(sq/2))-1


pos = (cx,cy)

dir = 'right'
size = 1
steps = 0

grid = [[0 for i in range(sq)] for j in range(sq)]
grid[cx][cy] = 1

sol = 0

for i in range(1, n):
	x,y = pos
	steps += 1
	if dir == 'right':
		pos = (x+1 , y)
		if steps == size:
			dir = 'up'
			steps = 0
	elif dir == 'up':
		pos = (x, y-1)
		if steps == size:
			dir = 'left'
			steps = 0
			size += 1
	elif dir == 'left':
		pos = (x-1, y)
		if steps == size:
			dir = 'down'
			steps = 0
	elif dir == 'down':
		pos = (x, y+1)
		if steps == size:
			dir = 'right'
			steps = 0
			size += 1
	g = 0
	x,y = pos
	for j in range(-1,2):
		for k in range(-1,2):
			if j != 0 or k != 0:
				g += grid[x+j][y+k]
	
	x,y = pos
	grid[x][y] = g
	if g > n and sol == 0:
		sol = g
	
# print('\n'.join([' '.join([str(y) for y in x]) for x in grid]))

x,y = pos
print('Part 1: ', pos, abs(x - cx) + abs(y - cy))
print('Part 2: ', sol)




