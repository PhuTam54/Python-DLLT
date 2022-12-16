#for a in range(0,3):
#	print(a)
#	for b in range(0,2):
#		print(b)
#
#print("\n---")
#for a in range(1,3):
#	for b in range(0,2):
#		print(b)
#	print(a)
#
#print("\n---")
#for a in range(0,3):
#	for b in range(0,2):
#		print(b)
#		print(a)

#for i in range(10):
#	if i == 5:
#		continue
#	print(i)
#
#print("\n---")
#
#for j in range(10):
#	if j == 6:
#		break
#	print(j)

s_denominator = 0

for i in range(100):
	if i == 1:
		continue
	if i % 2 == 0:
		continue

s_denominator = s_denominator + 1/i

s = 1 / s_denominator
s = round(s,2) 
print("S= "+ str(s))