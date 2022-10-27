##problem 1
##c ‘p’
##e ‘a’ &’ni’
##g ‘SPAM’
print(7//3)
s1 = "spam"
s2 = "ni!"

##problem 2
s2[:2].upper()
s1[:]
print('['+s1[:2]+','+s1[3:]+']')

##problem 3
##b

##Now
##is
##the
##winter
##of
##our
##discontent...

##c

##M ss ss pp

##e

##tf
##tfd
##tfds
##tfdsf
##tfdsfu


for w in "Mississippi".split("i"): 
	print(w, end=" ")

msg=""
for ch in "secret":
	msg = msg + chr(ord(ch)+1) 
	print (msg)

print("Grades=",end='')
x = 0
while x < 60:
	print('F',end='')
	x+=1

x=0
while x < 10:
	print('D',end='')
	x+=1
	
x=0
while x < 10:
	print('C',end='')
	x+=1
	
x=0
while x < 10:
	print('B',end='')
	x+=1
	
x=0
while x < 10:
	print('A',end='')
	x+=1
	
print(" ")
x = eval(input("Input numerical grade: "))
if x < 60:
	print("F")
if x > 59 and x <70:
	print("D")
if x > 69 and x <80:
	print("C")
if x > 79 and x <90:
	print("B")
if x > 89:
	print("A")
	
	
x=input("Enter a name: ")
x = x.lower()
sum=0
for i in x:
	sum+=ord(i)-96
print(sum)

def phrase_splitter():
	phrase=input("Enter a phrase or set of words: ")
	return phrase.split()
	
def char_parser(str):
	str=str.upper()
	print(str[0:1],end="")

phrase_list=phrase_splitter()
for x in phrase_list:
	char_parser(x)
	

	
