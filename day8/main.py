raw_input = open('data2.txt', 'r')
instructions = []
values = []
for line in raw_input:
	instruction, contents = line.split(' ')
	instructions.append(instruction)
	contents = contents.strip('\n')
	values.append(contents)


accumulator = 5
counter = 0
running = True



def decision(instruction, value, counter, accumulator):
	return{
		'acc': acc,
		'jmp': jump,
		'nop': no_op,
		'default': default,
	}.get(instruction, default)(value, counter, accumulator)

def acc(value, counter, accumulator):
	accumulator += int(value)
	instructions[counter] = 'Done'
	values[counter] = 'Done'

	return counter+1, accumulator

def jump(value, counter, accumulator):
	value2 = int(value)
	instructions[counter] = 'Done'
	values[counter] = 'Done'
	print("Jumping from " + str(counter) + " to " + str(counter + value2) + " because jump has a value of " + str(value) + " and ")
	print(value2)
	return counter + value2, accumulator

def no_op(value, counter, accumulator):
	instructions[counter] = 'Done'
	values[counter] = 'Done'
	return counter + 1, accumulator

def default(value, counter, accumulator):
	print("Using default with a value of " + str(value) + " and the accumulator at " + str(accumulator) + " at counter " + str(counter))
	return counter + 1, accumulator

while running:
	if ((instructions[counter] == 'Done') or (values[counter]) == 'Done'):

		running = False

		break

	counter, accumulator = decision(instructions[counter], values[counter], counter, accumulator)
	


print(accumulator)
#454 IS TOO LOW
#1935 ISN'T RIGHT
