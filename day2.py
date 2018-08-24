

chk = 0
sum = 0

file = open("./input/input2.txt", "r")
for s in file:
	s = s.strip()
	s = [int(x) for x in s.split()]
	
	minX = min(s)
	maxX = max(s)
	chk += maxX - minX
	
	for i in range(0, len(s) - 1):
		for j in range(i + 1, len(s)):
			if s[i] % s[j] == 0:
				sum += s[i]/s[j]
			elif s[j] % s[i] == 0:
				sum += s[j]/s[i]
	
print('Part 1: ', chk)
print('Part 2: ', sum)

file.close()