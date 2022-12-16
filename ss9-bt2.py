#2. Bài 02: 
#Viết chương trình nhập một số nguyên dương bất kỳ, tính tổng các chữ số của nó sử, dụng vòng  lặp for. 
n = int(input("Nhap mot so nguyen duong bat ky: "))
for i in range(n):
	n = int(n/100)
	n = n- n*100
	if n!=0:
		print(n)