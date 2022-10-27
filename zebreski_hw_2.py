import math as math
## this prints the variable i (1-5) times itself
for i in range(5):
	print(i *i)
## this prints the index of variable d though the entire array as well as puts a space after the number printed and keeps it on the same line
for d in [3,1,4,1,5]: 
	print (d, end=" ")
## this prints "Hello" 4 times
for i in range( 4): 
	print ("Hello")
#this prints 2 to the power of i as i acsends from 1-5
for i in range(5): 
	print(i, 2**i)
	
#1 a,c,e 	##7.4
print(4.0/10.0+3.5*2)
##8
print(abs(4-20//3)**3)
##11
print(3*10//3+10%3)

#question 2 b,c
n=1
print(n*(n-1)/2)
r = 5
print(math.pi*4*r)

#question 3 
#b 1:1  1 3:27  3 5:125 5 7:343 7  9:729 9
 
for i in [1,3,5,7,9]: 
	print(i, ":", i**3)
	print (i)

#c adds x+y every iteration but prints the iterable each time and counts by the parameter 2 until the third parameter 10. also prints "done" at the end of each iteration
x=2
y = 10
for j in range(0, y, x): 
	print(j, end="")
	print (x + y) 
	print ("done")
	
	
	
	
	
	
##page 80 , question 6
print("This program determines the slope between two points.")
x1=eval(input(print("Enter x coordinate 1 : ")))
x2=eval(input(print("Enter x coordinate 2 : ")))
y1= eval(input(print("Enter y coordinate 1 : ")))
y2= eval(input(print("Enter y coordinate 2 : ")))

slopeFloat=(x2-x1)/(y2-y1)

print("The slope is : " + str(slopeFloat))
##page 80 , question 7

print("This program determines the distance between two points.")
x1 = eval(input(print("Enter first x coordinates: ")))
x2= eval(input(print("Enter second x coordinates: ")))

y1 = eval(input(print("Enter first y coordinate: ")))
y2 = eval(input(print("Enter second y coordinate: ")))

ydifference = (y2-y1)**2
xdifference = (x2-x1)**2
sum = ydifference+xdifference


distance = math.sqrt(sum)
print("The distance is : " + str(distance))
