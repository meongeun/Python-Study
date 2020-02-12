print("hello")
data = "Hello World"
print(data)
print(data[2])
print(data[7])

data2 = "Hi %s!" % "ALex"
print(data2)
print('Hello')

def sum(i1, i2):
	result =0
	for i in range(i1,i2+1):
		result += i
	
	return result

def main():
	print("Sum for 1 to 10: ", sum(1,10))
	print("Sum for 20 t0 37: ", sum(20,37))
	print("Sum for 50 to 60: ", sum(50, 60))

main()

large = sum(99,100)
print(large)




