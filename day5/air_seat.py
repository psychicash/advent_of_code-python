seats = []

with open('data.txt', 'r') as fh:
		
		for line in fh:
			line = line.strip()
			seats.append(line)

total_rows = 128
total_columns = 8
highest_seat = (127*8) + 7

def convert_seat(seat):
	s_row = seat[:-3] 
	s_row = s_row.replace('F', '0')
	s_row = s_row.replace('B', '1')
	
	seat_c =  seat[-3:]
	seat_c = seat_c.replace('L', '0')
	seat_c = seat_c.replace('R', '1')
	
	s_row = int(s_row, 2)
	seat_c = int(seat_c, 2)

	seat_num = (s_row * 8) + seat_c

	return s_row, seat_c, seat_num


available_seats = {}

for x in range(highest_seat):
	available_seats[x] = 0

for seat in seats:
	row, col, num = convert_seat(seat)
	available_seats[num] = 1

possible_seat = []


for key in available_seats.keys():
	try:
		if ((available_seats[key-1] == 1) and (available_seats[key+1] == 1) and (available_seats[key] == 0)):
			possible_seat.append(key)
	except KeyError:
		continue

print(possible_seat)
