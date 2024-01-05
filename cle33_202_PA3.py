#-------------------------------------------------------------------------------
# Name: Courtney Le
# Programming Assignment 3
# Due Date: 02/28/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


def break_time(hours_worn, last_break):
    remainder = 1 #figures out if hours_worn/last_break was int or float
    result = 0 #ideal break time
    while remainder != 0: #will keep repeating until theres no remainder
        remainder = hours_worn % last_break #finds remainder of this
        if remainder == 0: #meaning: if dividing leads to whole num then..
            return result
        elif remainder != 0: #if value is float..
            hours_worn /= last_break #will divide and store back into var
            hours_worn = int(hours_worn) #turns into integer
            result += 1 #counts how many times goes through this elif

#extra/clarifying/detailed notes:
#int = integer (whole num)
#float = fraction/decimal (not a whole num)
#var = variable
#result is also num of times answer was a decimal (dec)
#explanation:
    #remainder used to find if hours_worn/last_break was int or dec
    #if it was an int, result will be returned
    #if not, it'll divide hours_worn and last_break
    #then store that value back into hours_worn
    #and will be turned into an integer
    #and since going through that elif means answer was
    #   a dec, result is added once (to count)
    #then loop will repeat until remainder is 0
    #   aka, until reaches whole number when dividing


def how_many_uruks(strength_values, init_fund_needed):
    budget = 0 #initial value
    result = 0 #how many times went through while loop
    for num in strength_values: #will loop through each strength_values
        remainder = num % 2 #calc odd or even
        if num == 0: #will do nothing for zeroes
            budget += 0
        elif remainder == 1: #for odd values
            budget += num #adds the odd values
        elif remainder == 0: #for even values
            budget *= num #multiplies even values
    while (budget - init_fund_needed) > 0: #keeps looping until cant sub
        budget -= init_fund_needed #subtracts fund from budget
        if (budget - init_fund_needed) > 0:
            init_fund_needed += 1 #fund will increase by 1
        result += 1 #counts number of uruk/how many times can be sub
    return result #result is returned aka num of uruks that can be made
#extra/clarifying/detailed notes:
#the for loop goes through each number in strength_value
#remainder finds whether or not the number was odd or even
#   and stores it back into remainder
#since 0s do nothing, goes first and makes it add 0 to budget
#then if it's odd, it'll have a remainder of 1
#so it'll add the number to the budget and store back into budget
#if remainder is 0, means num is even
#so it'll multiply the num to budget and store back into budget
#the for loop will keep going until there are no more values
#the while loop means while the budget is able to be subtracted
#   by the fund(without becoming negative), it'll keep looping
#then it subtracts the budget by the fund and stores it back
#if it is able to be subtracted again, the fund increases
#   incrementally by one
#the result counts how many times it has gone through the
#   while loop, which happens to be the number of uruks
#   able to be created


def years_to_rule(n1, n2, n3):
    result = 0 #initialize variable
    for i in range(n1): #calls each int from 0 to n1
        i += 1 #has the range start from 1 instead of 0
        for num in range(n2): #calls each int from 0 to n2
            num += 1 #range starts from 1
            product = i * num #multiplies int with num
            quotient = product // n3 #integer divides product
            result += quotient #adds all quotients together
    return result
#extra/clarifying/detailed notes:
#2 for loops used to go through all values of 1-n1 and 1-n2
#line 88 & 90 - since range usually starts from 0, have to put
#   that there so that it'll start from 1 instead 
#91-93 are calculating and storing values


def lotr_popularity(char_list):
    appearance1 = 0 
    points = 10 #rating for Gandalf
    rating1 = 0
    for x in char_list:
        if x == "Gandalf": #for when Gandalf appears in list
            appearance1 += 1 #counts num of appearance
    rating1 = appearance1 * points #total rating for Gandalf

    appearance2 = 0
    points = 20 #rating for Aragorn
    rating2 = 0
    for x in char_list:
        if x == "Aragorn": #when Aragorn appears in list
            appearance2 += 1 #counts each list appearance
    rating2 = appearance2 * points #total rating for Aragorn

    appearance3 = 0
    points = 5 #rating for Legolas
    rating3 = 0
    for x in char_list:
        if x == "Legolas": #for when Legolas's name appears in list
            appearance3 += 1 #counts num of appearances
    rating3 = appearance3 * points #total rating for Legolas

    mostPop = str()
    totalRating = rating1 + rating2 + rating3 #adds all ratings
    if appearance1 > appearance2 and appearance1 > appearance3:
        mostPop = "Gandalf" #for when Gandalf has most appearance
    elif appearance2 > appearance1 and appearance2 > appearance3:
        mostPop = "Aragorn" #for when Aragorn has most appearance
    elif appearance3 > appearance1 and appearance3 > appearance2:
        mostPop = "Legolas" #for when Legolas has most appearance
    
    result="Most Appeared: "+str(mostPop)+", "+"Popularity: "+str(totalRating)
    return result
#extra/clarifying/detailed notes:
#all the 'appearance' and 'rating' start off as 0 to initialize
#mostPop is initialized with line 127
#mostPop means most popular, the char name is assigned to mostPop when
#   a character has appeared the most out of the other 2 chars
#each 'rating' counts the total number of rating by multiplying 
#   the num of points each char receives by the num of appearances
#result uses concatenation for the return
