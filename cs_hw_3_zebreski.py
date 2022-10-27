def collectInput(inp):
	print(inp)

total_n=eval(input(fact("Please enter a total amount of numbers to be entered: ")))
sum=0
i=0
while i < total_n:
	sum += eval(input(fact("input number to add total: ")))
	i+=1
print("This is the sum :" + str(sum))


total_n=eval(input(print("Please enter a total amount of numbers to be averaged: ")))
i=0
sum=0
while i < total_n:
	sum += eval(input(print("input number to add total: ")))
	i+=1
print("This is the average float: " +str(float(sum/total_n)))


## chapter 4 discussion question 2
##a
##b
##c
##d
##e
##f
##g
