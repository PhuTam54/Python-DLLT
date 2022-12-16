import datetime 

def ask_info():
	first_name = input("Your first name is: ")
	last_name = input("Your last name is: ")
	year_born = int(input("When you were born: "))
	meter_heigh = float(input("Your heigh (meter): "))
	is_male = ask_yes_no("Are you male? (Yes/No) ")
	is_Vietnamese = ask_yes_no("Do you love Viet Nam? (Yes/No) ")
	return first_name, last_name, year_born, meter_heigh, is_male, is_Vietnamese

def calc_age(year_born):
	now = datetime.datetime.now()
	CURRENT_TiME = now.year

	return CURRENT_TiME - year_born 

def meter_to_feet(meter):
	METER_TO_FEET = 3.2808399
	feet = float(meter) * METER_TO_FEET
	feet = round(feet,2)
	return feet

def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if answer == "Yes":
			return True
		elif answer == "No":
			return False
		else:
			continue

def print_high_info(is_male, feet_heigh):
	if is_male == True:
		if feet_heigh > 6.0 and feet_heigh <=6.5:
			print("You are tall as a man")
		elif feet_heigh > 6.5:
			print("You are", end=" ")	
			for i in range(10):
				print("very", end =(" "))
			print("tall as a man")
		else:
			print("You are short as a man")

	if is_male == False:
		if feet_heigh >5.7:
			print("You are tall as a woman")
		elif feet_heigh <5:
			print("You are", end=(" "))
			j =0
			while j <10:
				j +=1
				print("very", end =(" "))
			print("short as a woman")	
		else:
			print("You are short as a woman")

def print_infor(first_name, last_name, age, feet_heigh, is_male, is_Vietnamese):
	now = datetime.datetime.now()
	CURRENT_TiME = now.year
	print("\n")#, end=" ")
	for a in range(10):
		print("-", end = " ")
	print("\nYour name is {0} {1}".format(first_name,last_name))
	print("{0} {1} is {2} years old in {3}".format(first_name,last_name,age,CURRENT_TiME))
	print("You are " + str(feet_heigh) + " feet tall" )
	
	if is_Vietnamese == True:
		print("You love Viet Nam so much")
	else:
		print("Oh man:((")
	print_high_info(is_male, feet_heigh)

def main():
	first_name, last_name, year_born,meter_heigh, is_male, is_Vietnamese = ask_info()
	age = calc_age(year_born)
	feet_heigh = meter_to_feet(meter_heigh)
	print_infor(first_name, last_name, age, feet_heigh, is_male, is_Vietnamese)

main()