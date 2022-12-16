import datetime

def main():
	firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_info()
	age = calc_age(year_born)
	height_feet= meter_to_feet(height_meter)
	print_person_infor(firstname, lastname, age, height_feet, is_male,is_vietnamese)

def ask_person_info():
	firstname = input("Your firstname: ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male? (yes/no): ")
	is_vietnamese = ask_yes_no("Do you love Viet Nam? (yes/no): ")
	return firstname, lastname, year_born, height_meter, is_male, is_vietnamese

def print_person_infor(first_name, last_name, age, feet_heigh, is_male, is_Vietnamese):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	for a in range(10):
		print("-", end = " ")
	print("\nYour name is {0} {1}".format(first_name,last_name))
	print("{0} {1} is {2} years old in {3}".format(first_name,last_name,age,CURRENT_YEAR))
	print("You are " + str(feet_heigh) + " feet tall" )
	
	if is_Vietnamese == True:
		print("You love Viet Nam so much")
	else:
		print("Oh man:((")
	print_person_height(is_male, feet_heigh)

def calc_age(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	year_born = int(year_born)
	age = CURRENT_YEAR - year_born
	return age

def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			continue

def meter_to_feet(meter):
	METER_TO_FEET = 3.281
	meter = float(meter)
	feet = meter * METER_TO_FEET
	feet = round(feet,1)
	return feet

def print_person_height(is_male, height_feet):
	if is_male == True:
		if height_feet > 6.5:
			print("You are", end=" ")
			for i in range(10):
				print("very", end=" ")
			print("tall as a man")
		elif height_feet > 6.0:
			print("You are tall as a man")
		else:
			print("You are short as a man")

	else:
		if height_feet > 5.7:
			print("You are tall as a girl")
		elif height_feet < 5.0:
			print("You are", end=" ")
			i=0
			while i<10:
				print("very ", end = "")
				i+=1
			print("short as a girl")
		else:
			print("You are short as a girl")

main()