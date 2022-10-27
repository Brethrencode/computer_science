# How is exception handling using try except similar to and
# different from handling exceptional cases using ordinary
# decision structures (variations on if)?
#
# Exception handling tries a block of code and if there is an error
# it can catch it in except and run alternate code and continue the program.
# Otherwise , it could crash and end abruptly.
#
#
#


#This is a deccision tree for academic grades , integers return letter grades
def exam_Score():
    inp = eval(input('Enter a grade as a number: '))
    if inp >= 90:
        print('A')
    elif 80 <= inp <= 89:
        print('B')
    elif (inp >= 70) and (inp <= 79):
        print('C')
    elif 60 <= inp <= 69:
        print('D')
    elif inp < 60:
        print('F')

## This removes a 0 from in front of the time and also removes the colon
def first_digit_zero_checker(time):
    x = 0
    if time[0] == '0':
        time = time[1:]

    while x < len(time):
        if time[x] ==':':
            time = time.replace(":", "")

        x += 1

    return time
##This converts the currency to a string with a decimal point in the correct position
def currency_conversion(total):
    a = str(total)
    special_character_added = a[:2] + '.' + a[2:]
    return special_character_added
##This takes 2 inputs of time and returns the wages a babysitter can earn by the times they have spent working
def babysitter():
    rate_1 = 250
    rate_2 = 175
    regular_rate_total = 0
    overtime_total = 0
    start_time = input("Enter a start time as military time: ")
    end_time = input('Enter an end time as military time: ')

    a = eval(first_digit_zero_checker(start_time))
    b = eval(first_digit_zero_checker(end_time))

    if b > 2100:
        overtime_total += b - 2100

    regular_rate_total += (2100 - a)
    total = ((regular_rate_total*rate_1)//100 + (overtime_total*rate_2)//100)
    total = currency_conversion(total)
    print('This is the total the babysitter has earned: ' + str(total))

#This calculates wether a person is eligible for senator/representative
# by taking years as input and measuring them against requirements
def US_Senator():
    x = -1
    while x < 0:
        a = eval(input("Enter an age: "))
        b = eval(input('Years of citizenship: '))
        if a >= 25 and b >= 7:
            print('Representative eligible.')
        if a >= 30 and b >= 9:
            print('Senator eligible.')
        else:
            print('Not eligible.')

if __name__ == '__main__':
    babysitter()
    exam_Score()
    US_Senator()