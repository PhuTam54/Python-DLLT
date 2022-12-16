colors = ["red", "green", "blu"]

colors.append("heheh")

for i in range(len(colors)):
	print(colors[i])

print("---")
last_index = len(colors)-1
print(colors[-1],"\n")

print(colors)
try:
	colors.remove("green")
except:
	print("Not exist")
print(colors, "\n")

colors.pop()
print(colors)

print("---")
colors.append("red")
print(colors)

print("---")
#find index of "red" in list
try:
	print(colors.index("red"))
except:
	print("Not exist")

colors.insert(2,"pink")
print(colors)

#find number of occurance of "red"
def index():
	red_index = []
	for i in range(len(colors)):
		if colors[i]=="red":
			red_index.append(i)
	print("---")
	print("The word 'red' occurs at the following in dex:",red_index)

	print("How many time 'red' occurs:",colors.count("red"))
index()
#change the third element to "Phu Tam"
colors[2]="Phu Tam"
print(colors)

index()

print("---")
a = [1,3,4,5,6,3,5,7,4,3,9,8,10,6]
a.sort()
print(a)
a[3]="Tran Thuy"
print(a)