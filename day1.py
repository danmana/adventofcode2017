

def sumOf(s, offset):
	sum = 0
	n = len(s)
	for i in range(0, len(s)):
		if s[i] == s[(i + offset) % n]:
			sum += int(s[i])
	
	return sum

	
	
file = open("./input/input1.txt", "r")
for s in file:
	s = s.strip()
	
	print('Part 1: ', sumOf(s, 1))
	print('Part 2: ', sumOf(s, int(len(s)/2)))
	

file.close()