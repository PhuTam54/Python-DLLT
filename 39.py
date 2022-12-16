
with open("ok.txt", "w") as file:
	file.write("ccccc\n")
	file.write("qqqqq\n")

with open("ok.txt", "w") as file:
	file.write("okok\n")
	file.write("heheh\n")

with open("ok.txt", "a") as file:
	file.write("Phu Tam\n")
	file.write("Tran Thuy")

with open("ok.txt", "r") as file:
	data = file.read()
	print(data)

with open("data.txt", "w") as file:
	file.write("okokk")
with open("data.txt", "w") as file:
	file.write("kokoko\n")
with open("data.txt", "a") as file:
	file.write("hehehe")
with open("data.txt", "r") as file:
	data = file.read()
	print(data)



#def main():
#	hsa_name = "Tam"
#	hsa_T = 9
#	hsa_V = 7
#	hsb_name = "Thuy"
#	hsb_T= 8
#	hsb_V=10
#	print_student(hsa_name, hsa_T, hsa_V)
#	print_student(hsb_name, hsb_T, hsb_V)
#
#def print_student(name, T, V):
#	print("Student name: "+name)
#	print("Math: "+str(T))
#	print("Literature: "+str(V))
#
#main()