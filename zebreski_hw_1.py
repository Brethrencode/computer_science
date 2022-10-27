##prints one string
print("hello world!")
##printa2 strings on the same line
print("hello","world!")

##prints an integer
print(3)
##prints a float
print(3.0)

##prints an addition math problem
print(2+3)
##prints a floating point result addition problem of two floats
print(2.0 +3.0)

##prints two strings
print("2"+"3")
##prints two strings plus a math result of an addition problem. the first part is a string and the second is the problem
print("2 + 3 =",2+3)
##prints a mutiplication result

print(2*3)
## prints a number to the nth power
print(2**3)
##prints the number result of the division problem as a floating point due to remainder
print(7/3)
## prints the whole number result without remainder
print(7 // 3)


## collects data for conversion
miles = eval(input("Enter number of miles: "))
## prints kilometer calulation
print(miles*.62,"kilometers")

n = eval(input("How many numbers should I print? "))
x = eval(input("Enter a number from 0-1"))
for i in range(n):
  x = 3.9 * x * (1 - x) 
  print(x)
  
t = eval(input("What is the number of years the money will be compounded for?"))
p=10000
n=12
r=.08
total = r/n
total +=1
total **= (n*t)
total *= p
print(total)
##formula for compound interest
print(p*((1+(r/n))**(n*t)))
  
## farenheight conversion calculator from book
def main():
	celsius = 0
	try :
		celsius = eval(input("What is the Celsius temperature? "))
		fahrenheit = 9/5 * celsius + 32
		print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
	except:
		print('Please only use numbers up to 3 digits')

main()
