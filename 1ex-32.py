def main():
	APPLE_PRICE = 22 #k VND
	apple_weigh = float(input("Enter weigh of apples (Kg): "))
	money_given = float(input("Total money customer give you (k VND): "))
	
	total = calc_money(apple_weigh, APPLE_PRICE)
	money_left = money_return(money_given,total)
	
	print("---")
	print("Total money:",total, "k VND")
	if money_left ==-1:
		print("Not enough money")
	else:
		print("You need to return to customer:", money_left, "k VND")
		print_return_info(money_left)

def calc_money(apple_weigh, APPLE_PRICE):
	total = apple_weigh * APPLE_PRICE
	total = round(total, 2)
	return total

def money_return(money_given, total):
	money_back = money_given - total
	money_back = round(money_back, 2)
	if money_back <0:
		return -1
	else:
		return money_back

def print_return_info(money_left):
	count500 = int(money_left/500)
	money_left = money_left- count500*500
	if count500!=0:
		print("500k:", count500)

	count200 = int(money_left/200)
	money_left = money_left- count200*200
	if count200!=0:
		print("200k:", count200)

	count100 = int(money_left/100)
	money_left = money_left- count100*100
	if count100!=0:
		print("100k:", count100)

	count50 = int(money_left/50)
	money_left = money_left- count50*50
	if count50!=0:
		print("50k:", count50)

	count20 = int(money_left/20)
	money_left = money_left- count20*20
	if count20!=0:
		print("20k:", count20)

	count10 = int(money_left/10)
	money_left = money_left- count10*10
	if count10!=0:
		print("10k:", count10)

	count5 = int(money_left/5)
	money_left = money_left- count5*5
	if count5!=0:
		print("5k:", count5)

	count2 = int(money_left/2)
	money_left = money_left- count2*2
	if count2!=0:
		print("2k:", count2)

	count1 = int(money_left)
	if count1!=0:
		print("1k:", count1)

main()