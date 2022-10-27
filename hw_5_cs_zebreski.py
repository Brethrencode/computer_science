from graphics import *
import math
def animals(animal):
    ##match case for each animal
     match animal:
        case "cow":
            print('The cow goes moo')
        case "dog":
            print('The cow goes bark')
        case "snake":
            print('The cow goes hsss')
        case "cat":
            print("The cat goes meow")
        case "chicken":
            print('The cow goes cluck')
##takes list and sums it using a for loop
def sumList(numb):
    sum = 0
    for i in range (0,len(numb)):
        sum += numb[i]
    print(sum)
## takes a number as parameter and makes a list of strings from user input
def getSomeStrings(numbOfStrings):
    listOfStrings=[]
    for i in range(0, numbOfStrings) :
        listOfStrings.append(input('Please input a string: '))
    return listOfStrings

## asks user to input numbers to average
def computeAverage():
    total_n = eval(input("Please enter a total amount of numbers to be entered: "))
    sum = 0
    i = 0
    while i < total_n:
        sum += eval(input("input number to add total: "))
        i += 1
    return sum/total_n
##function that returns slope as a string
def slope(x,y):
    return str(y//x)
##function that returns distance or length as a string
def distance(x,y):
    return str(math.sqrt((x ** 2) + (y ** 2)))

##function calls
animals('cow')
animals('dog')
animals('snake')
animals('cat')
animals('chicken')

numbers = [7,6,5,4,3,2,1]
sumList(numbers)
## asks for number of strings and evluates as an integer for the function
str_list = getSomeStrings(eval(input('How many strings would you like to input?')))
print(str_list)

##chapter 3 question 14


##loop to input numbers

average = str(computeAverage())

print("This is the average :" + average)

## chapter 4 exercise 8
def main():
    b = False
    win = GraphWin('Slope,Length & midpoint of a line',500,500)
    while b != True:
        p = win.getMouse()
        c = win.getMouse()
        print(p)
        dx = p.getX() - c.getX()
        print(dx)
        dy = p.getY() - c.getY()
        print(dy)
        slp = slope(dx,dy)
        dst = distance(dx,dy)
        midpointX = ((p.getX()+c.getX())//2 )
        midpointY = ((p.getY()+c.getY())//2 )
        midpt = Point(midpointX,midpointY)
        print("Slope is "+ slp)
        print("Length is " + dst)

        label = Text(Point(100, 120), "Slope is:  "+ str(dy//dx))
        label2 = Text(Point(100, 110), "Length is:  "+ str(math.sqrt((dx**2) + (dy**2))))
        label.draw(win)
        label2.draw(win)

        label_midpoint = Text(Point(midpointX,midpointY -10),'Midpoint is:  ' + str(midpt))
        label_midpoint.setTextColor('black')
        label_midpoint.draw(win)

        circ=Circle(midpt,3)
        circ.setOutline('cyan')
        circ.setFill('cyan')
        circ.draw(win)

        line = Line(p,c)
        line.setOutline("red")
        line.draw(win)

        answer=input("Do you wish to continue?")
        if answer == "No":
            win.close()
            b = True
        win.clear(win)

main()


