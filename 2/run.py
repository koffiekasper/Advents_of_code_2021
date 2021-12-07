def partone():
	fhandle = open("./input.txt")
	dep = 0
	hor = 0
	for line in fhandle:
		line = line.strip()
		words = line.split()
		val = int(words[1])
		if words[0] == "forward":
			hor += val
		elif words[0] == "down":
			dep += val
		elif words[0] == "up":
			dep -= val
	print(f"Solution: {dep*hor}")

def parttwo():
	fhandle = open("./input.txt")
	aim = 0
	hor = 0
	dep = 0
	for line in fhandle:
		line = line.strip()
		words = line.split()
		val = int(words[1])
		if words[0] == "forward":
			hor += val
			dep += val*aim
		elif words[0] == "down":
			aim += val
		elif words[0] == "up":
			aim -= val
	print(f"Solution: {dep*hor}")
	
partone()
parttwo()