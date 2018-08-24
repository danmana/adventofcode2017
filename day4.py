valid = 0
valid2 = 0

def hasAna(s):
	for i in range(len(s)-1):
		for j in range(i+1, len(s)):
			a = [ch for ch in s[i]]
			b = [ch for ch in s[j]]
			
			a.sort()
			b.sort()
			
			a = ''.join(a)
			b = ''.join(b)
			
			if a == b:
				return True
	return False

file = open("./input/input4.txt", "r")
for s in file:
	s = s.strip()
	s = s.split()
	s2 = set(s)
	
	if len(s) == len(s2):
		valid += 1
		
		if not hasAna(s):
			valid2 += 1
		
			
	
print('Part 1: ', valid)
print('Part 2: ', valid2)

file.close()