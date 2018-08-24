
file = open("./input/input5.txt", "r")
input = [int(line.strip()) for line in file]
file.close()

s = [x for x in input]
steps = 0
pos = 0


while pos >= 0 and pos < len(s):
	steps += 1

	jump = s[pos]
	s[pos] += 1
	pos += jump


print('Part 1: ', steps)	


s = [x for x in input]
steps = 0
pos = 0

while pos >= 0 and pos < len(s):
	steps += 1

	jump = s[pos]
	
	if jump >= 3:
		s[pos] -= 1
	else:
		s[pos] += 1
	
	pos += jump
	

print('Part 2: ', steps)	
