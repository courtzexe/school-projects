#-------------------------------------------------------------------------------
# Name: Courtney Le
# Programming Assignment 1
# Due Date: 2/7/2022
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

#greet the user
print("Sage's Wedding Cake Price Calculator")
#get input of number of people attending
attendees = int(input("Total People Attending: "))
print("----------------------------------------")
#costs
#consultants' pay per hour
consultant_pay = 12.50
#bakers' pay per hour
bakers_pay = 15.00


#cake A
print("Cake A")

#cost of labor
#calculations for pays
bakers_pay_cakeA = float(bakers_pay * 15)
consultant_pay_cakeA = float(consultant_pay * 1)
#adding consultant & baker pay & calculating with # of attendees
labor_cost_cakeA = float(((bakers_pay_cakeA + consultant_pay_cakeA) / 30) * attendees)
print(str("Labor Cost:     \t$") + str(round(labor_cost_cakeA, 2)))

#cost to make the cake
#ingredients' cost (for 30 people)
ingredients_cost = 35
#attendees taken into account of ingredients' cost
ingredients_cost /= 30 
ingredients_cost *= int(attendees)
#adding ingredients cost to labor cost
cost_to_makeA = float(labor_cost_cakeA) + float(ingredients_cost)
print(str("Cost to Make:   \t$") + str(round(cost_to_makeA, 2)))

#charge to customer
#find profit amount then add to cost to make 
profitA = float(float(cost_to_makeA) * 0.1)
customer_charge = float(float(cost_to_makeA) + float(profitA))
print(str("Charge Customer: \t$") + str(round(customer_charge, 2)))
print("----------------------------------------")


#cake B
print("Cake B")

#cost of labor (for cake b)
#number of hours it took for cake B to be made
cake_hours = 14
#standard formula for how much bakers' pay would cost
bakers_pay_cost = float(bakers_pay) * float(cake_hours)
#number of hours consulted about cake
consultant_hours = 2
#standard formula for consultant's pay cost
consultant_pay_cost = float(consultant_pay) * float(consultant_hours)
#total labor cost
labor_cost = float(((bakers_pay_cost + consultant_pay_cost) / 30) * attendees)
print(str("Labor Cost:     \t$") + str(round(labor_cost, 2)))

#cost to make the cake
#ingredients' cost (for 30 people)
ingredients_cost = 30
#num of attendees taken into account of ingredients' cost
ingredients_cost /= 30 
ingredients_cost *= int(attendees)
#adding ingredients to labor cost
cost_to_make = (float(labor_cost) + float(ingredients_cost))
print(str("Cost to Make:   \t$") + str(round(cost_to_make, 2)))

#charge to customer
#profit amount in decimals
profit_decimal = 0.1
#find profit amount (10% of cost to make value) then add to cost to make 
profit = float(cost_to_make) * float(profit_decimal)
customer_charge = (float(cost_to_make) + float(profit))
print(str("Charge Customer: \t$") + str(round(customer_charge, 2)))
print("----------------------------------------")


#cake c
print("Cake C")

#cost of labor (for cake c)
#number of hours it took for cake B to be made
cake_hours = 16
#standard formula for how much bakers' pay would cost
bakers_pay_cost = float(bakers_pay) * float(cake_hours)
#number of hours consulted about cake
consultant_hours = 1.5
#standard formula for consultant's pay cost
consultant_pay_cost = float(consultant_pay) * float(consultant_hours)
#total labor cost
labor_cost = float(((bakers_pay_cost + consultant_pay_cost) / 30) * attendees)
print(str("Labor Cost:     \t$") + str(round(labor_cost, 2)))

#ingredients' cost (for 30 people)
ingredients_cost = 40
#num of attendees taken into account of ingredients' cost
ingredients_cost /= 30
ingredients_cost *= int(attendees)
#adding ingredients to labor cost
cost_to_make = (float(labor_cost) + float(ingredients_cost))
print(str("Cost to Make:   \t$") + str(round(cost_to_make, 2)))

#charge to customer
#profit amount in decimals
profit_decimal = 0.1
#find profit amount (10% of cost to make value) then add to cost to make 
profit = float(cost_to_make) * float(profit_decimal)
customer_charge = (float(cost_to_make) + float(profit))
print(str("Charge Customer: \t$") + str(round(customer_charge, 2)))

#for cake b and c, the programmer is able to just input 
# in the values of the time it takes to make the cake 
# (cake_hours), the amount of time the consultant spent 
# (consultant_hours), and the cost of the ingredients 
# (ingredients_cost) and this code would be able to 
# calculate the values for any cake based on any of 
# the inputted values :D