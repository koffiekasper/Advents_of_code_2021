def partone():
	# Creates 'File handle' object. Allows us to read/write files
	fhandle = open("./input.txt")

	# Initialize values we're working  with
	prev = -1
	up = 0
	down = 0

	# Will loop through every line in our file handle. We can access the current lien with the 'line' variable (for LINE in fhandle)
	for line in fhandle:
		# doing .strip() on a string will rid it of any 'newline characters'. (The invisible RETURN character that do a newline)
		# This means that instead of 420\n We would just be left with 420
		# Doing int() around it converts string that line.strip() outputs to a string. So "420" would be 420
		val = int(line.strip())

		# you can figure the if else shit out
		if prev == -1:
			prev = val
		else:
			if val < prev:
				down += 1
			if val > prev:
				up += 1
			prev = val
	# print results
	print(f"Up: {up} \nDown: {down}")

def parttwo():
	fhandle = open("./input.txt")

	valList = []
	current = 0
	for line in fhandle:
		current = int(line.strip())
		valList.append(current)
	
	inc = 0
	dec = 0	
	current = 0
	prev = 0

	for i in range(len(valList)):
#		if i < 4:
#			continue
		current = valList[i] + valList[i-1] + valList[i-2]
		prev = valList[i-1] + valList[i-2] + valList[i-3]
		print(current, prev)
		if current > prev:
			inc += 1
		if current < prev:
			dec += 1

	print(f"Up: {inc} \nDown: {dec}")



partone()
parttwo()