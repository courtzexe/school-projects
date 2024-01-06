#-------------------------------------------------------------------------------
# Name: Courtney
# Programming Assignment 7
# Due Date: 04/18/2022
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


def fraction_count(num1, num2):
    if num1 % num2 == 0: #if there is no remainder (reaches whole num)
        return 0 #returns 0
    else:
        quot = int(num1 / num2) #finds quotient and rounds down
        return (1 + fraction_count(quot, num2)) #1 keeps count & recursion


def concat_order(str1, str2):
    if len(str1) == 0 or len(str2) == 0: #once list ends, returns nothing
        return '' #once it goes through the whole string
    else: #slices the list & gets first chartacter
        return str1[0] + str2[0] + concat_order(str1[1:], str2[1:]) 


def sum_product(some_list, i, j):
    if i > j: #if the indexes cross in the list
        return 0 #ends the recursion
    elif i == j: #if it is odd 
        return some_list[i] #returns the mid num
    else: #the recursion, finds product then adds each
        return some_list[i] * some_list[j] + sum_product(some_list, i+1, j-1)

print(sum_product([23, 4, 12, 4, 12, 3, 5, 1, 6], 2, 6)) #84
print(sum_product([23, 4, 12, 4, 12, 3, 5, 1, 6], 5, 5)) #3
print(sum_product([1, 2, 3, 4, 5, 6], 4, 2)) #0

def calc_res(some_list, res=0):
    if len(some_list) == 0: #ends once reaches end of some_list
        return res #returns res, which was the end val after everything
    elif some_list[0] == 0: #if val in list was 0
        res = res #do nothing, keep res being same val
    elif some_list[0] % 2 == 1: #if val is odd
        res += some_list[0] #add val and store into res
    elif some_list[0] % 2 == 0: #if val is even
        res *= some_list[0] #multiply val and store into res
    return calc_res(some_list[1:], res) #slice list and use new res val


