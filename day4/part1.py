'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
data_list = []
global VALID_PASSPORTS
VALID_PASSPORTS = 0




class passport:
	def __init__(self, byr = None, iyr = None, eyr = None, hgt = None, hcl = None, ecl = None, pid = None, cid = None):
		self.traits = []
		self.byr = byr
		self.iyr = iyr
		self.eyr = eyr
		self.hgt = hgt
		self.hcl = hcl
		self.ecl = ecl
		self.pid = pid
		self.cid = cid

		self.traits.append(self.byr)
		self.traits.append(self.iyr)
		self.traits.append(self.eyr)
		self.traits.append(self.hgt)
		self.traits.append(self.hcl)
		self.traits.append(self.ecl)
		self.traits.append(self.pid)

		self.isvalid = self.validate()
		
	
	def validate(self):
		print("Traits")
		print(self.traits)
		for trait in self.traits:
			print(trait)
			print(type(trait))
			if (trait == None):
				return False
		else:
			global VALID_PASSPORTS
			VALID_PASSPORTS += 1
			return True

	def __str__(self):
		return 'Passport(byr: '+ str(self.byr) + ', iyr: ' + str(self.iyr) + ', eyr: ' + str(self.eyr) + ', hgt: ' + str(self.hgt) + ', hcl: ' + str(self.hcl) + ', ecl:' + str(self.ecl) + ', pid:' + str(self.pid) + ', is_valid: ' + str(self.isvalid) + ')'


				
def process_data():
	

	with open('data.txt', 'r') as fh:
		d = {}
		for line in fh:
			line = line.rstrip()
			if (len(line) == 0):
				create_entry(d)
				d.clear()
				continue
			else:
				working_line = line.rsplit(' ')
				for l in working_line:
					temp_line = l.rsplit(':')
					key = temp_line[0]
					val = temp_line[1]
					d[key] = val

	#print(data_list)
	for d in data_list:
		print(d)
	global VALID_PASSPORTS
	print(VALID_PASSPORTS)
				
def create_entry(my_dict):
	byr = my_dict.get('byr', None)
	iyr = my_dict.get('iyr', None)
	eyr = my_dict.get('eyr', None)
	hgt = my_dict.get('hgt', None)
	hcl = my_dict.get('hcl', None)
	ecl = my_dict.get('ecl', None)
	pid = my_dict.get('pid', None)
	cid = my_dict.get('cid', None)

	
	data_list.append(passport(byr, iyr, eyr, hgt, hcl, ecl, pid, cid))
	

''''
guess 1 = 284 - too high
guess 2 = 259 - too low
'''
process_data()
