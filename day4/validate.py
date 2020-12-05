
def val_byr(sus_byr):
	#byr (Birth Year) - four digits; at least 1920 and at most 2002.
	if (len(sus_byr) == 4):
		sus_byr = int(sus_byr)
		if ((sus_byr >= 1920) and (sus_byr <= 2002)):
			return True
	return False

def val_iyr(sus_iyr):
	#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	if (len(sus_iyr) == 4):
		sus_iyr = int(sus_iyr)
		if ((sus_iyr >= 2010) and (sus_iyr <= 2020)):
			return True
	return False
	
def val_eyr(sus_eyr):
	#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	if (len(sus_eyr) == 4):
		sus_eyr = int(sus_eyr)
		if ((sus_eyr >= 2020) and (sus_eyr <= 2030)):
			return True
	return False



def val_invalid(x):
	return False

def val_hgt_cm(sus_hgt):
	try:
		x = int(sus_hgt)
		
		if ((x >= 150) and (x <= 193)):
			return True
		else:
			raise
	except:
		return False

def val_hgt_in(sus_hgt):
	try:
		x = int(sus_hgt)
		
		if ((x >= 59) and (x <= 76)):
			return True
		else:
			raise
	except:
		return False

def val_hgt(sus_hgt):
	#hgt (Height) - a number followed by either cm or in:
	#If cm, the number must be at least 150 and at most 193.
	#If in, the number must be at least 59 and at most 76.
	return{
		'cm': val_hgt_cm,
		'in': val_hgt_in
	}.get(sus_hgt[-2:], val_invalid)(sus_hgt[:-2])




def val_hcl(sus_hcl):
	#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	try:
		if (len(sus_hcl) == 7):
			if (sus_hcl[0] == '#'):
				for char in sus_hcl:
					try:
						x = int(char)
					except(ValueError):
						return {
							'a': True,
							'b': True,
							'c': True,
							'd': True,
							'e': True,
							'f': True,
						}.get(char, None)

					else:
						return False
			else:
				raise ValueError
		else:
			raise ValueError
	except:
		return False




def val_ecl(sus_ecl):
	#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	return{
		'amb': True,
		'blu': True,
		'brn': True,
		'gry': True,
		'grn': True,
		'hzl': True,
		'oth': True
	}.get(sus_ecl, False)
	

def val_pid(sus_pid):
	#pid (Passport ID) - a nine-digit number, including leading zeroes.
	try:
		if (len(sus_pid) == 9):
			x = int(sus_pid)
			return True
		else:
			raise ValueError
	except (ValueError):
		return False
	


def switch_traits(trait_name, trait):
	print(trait_name)
	print(trait)
	return {
		'byr': val_byr,
		'iyr': val_iyr, 
		'eyr': val_eyr, 
		'hgt': val_hgt, 
		'hcl': val_hcl, 
		'ecl': val_ecl, 
		'pid': val_pid
	}.get(trait_name, lambda: None)(trait)
