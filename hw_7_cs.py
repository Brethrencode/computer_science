## definite loop vs. indefinite loop
## definite loops have a controlled count with a certain set of instructions  and while loops continue
## Until a certain condition is met.
##------------------------------------
## for loop vs. while loop
## For loop is used when the number of iterations are known and a while loop is indefinite.
## For loops are for arrays and code to be executed n times. While loops are for reading files
## and collecting input.
##------------------------------------
## interactive loop vs. sentinel loop
##
## The sentinel loop continues until it collects special data that signals the end.
##
## Users can be unpredictable so limitations on input in a interactive loop may be used to collect input.
## Such as a number between 1-100. The loop can continue until the actual parameter is satisifed within the limits.
##-------------------------------------
## sentinel loop vs. end-of-file loop
##
##  An example of a sentinel loop is a loop waiting for an event. For example " while True :" is the beginning,
##  True is unchanging. While an end of file loop continues until there is no more data left to process.
##
##

##  P   Q    a) not (P and Q)
##  T   T           F
##  T   F           F
##  F   T           F
##  F   F           T

##  P   Q    b) (notP)andQ
##  T   T           F
##  T   F           F
##  F   T           T
##  F   F           F

##  p   q    c) (not P) or (not Q )
##  T   T           F
##  T   F           T
##  F   T           T
##  F   F           T

##  P   Q    R   d) (PandQ)orR
##  T   T     T                 T
##  T   F     T                 F
##  T   T     F                 T
##  F   T     T                 F
##  F   F     T                 F
##  T   F     F                 F
##  F   F     F                 F
##  F   T     F                 T

##  P   R     Q       e) (PorR)and(QorR)
##  T   T     T                 T
##  T   F     T                 F
##  T   T     F                 F
##  F   T     T                 T
##  F   F     T                 F
##  T   F     F                 F
##  F   F     F                 F
##  F   T     F                 T <---R and R are both true
##



def while_loops():
    sum = 0
    x = 0
    n = eval(input('Enter a number: '))
    ##This loop sums the first n numbers
    while x <= n:
        sum += x
        x += 1
    print('The first ' + str(n) + ' numbers sum to : ' + str(sum))

    new_total = n * 2 - 1
    x = 0
    ##This loop sums the first n*2-1 odd numbers
    while x <= new_total:
        if x %2 == 1:
            sum += x
        x += 1
    print('The first ' + str(new_total) + ' odd numbers sum to : ' + str(sum))

    x = 0
    sum = 0
    total = n
    ##This loop determines how many times n can be divided by 2 as a whole number
    while x < n:
        if total / 2 >= 1:
            total /= 2
            sum += 1
            x+=1
        elif total / 2 == 0:
            sum += 1
            break
        x += 1
    print('The number of times ' + str(n) + ' can be divided as a whole number: ' + str(sum))




def fibonacci(n):
    print(str(0)+' '+str(1),end=" ")
    first = 0
    second = 1

    while n > 2:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        n -= 1
    print("\nThis is the final number in 'n'th place: " + str(second))
##This function is the syracuse sequence that continues until a number reaches 1
def syracuse_sequence(n):
    while n != 1:
        if n%2 == 0 :
            n /= 2
        else:
            n = (n*3) + 1
        print(str(n), end=" ")
##main function
if __name__ == '__main__':
    while_loops()
    fibonacci(eval(input("Enter a number for the fibonacci sequence: ")))
    syracuse_sequence(eval(input("Enter a number for the syracuse sequence: ")))
