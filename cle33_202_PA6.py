#-------------------------------------------------------------------------------
# Name: Courtney
# Programming Assignment 6
# Due Date: 04/11/2022
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


def fullCoverageClearance(dataDict = 0): #sets default val for when empty
    l = [] #list of booleans for each person
    if dataDict == 0: #if there is nothing in dataDict
        l = None #returns none as boolean
    else: #if there are inputs for dataDict
        for person in dataDict: #goes through people
            sum = 0 #initializes
            for money in dataDict[person]['Paid']: #each person's paid $
                sum += money #sums all their money
            if sum >= 3000: #if they qualify
                l.append(True) #true for qualifying
            elif sum < 3000: #if $ too little
                l.append(False) #does not qualify so false
    return l #returns the list of booleans


def buildCoverageDictionary(paidList):
    dict = {} #creates new dict
    for lst in paidList: #for each list in the list of lists
        payments = [] #creates new list 
        for i in range(1, len(lst)): #goes through each $ paid
            payments.append(lst[i]) #adds each payment
        dict[lst[0]] = {"Paid" : payments} #puts all together in dict
    return dict #returns the new dict w everything


def createNewCoverageList(namesList = 0, paymentList = 0):
    totalList = [] #the overall list that will be returned
    if namesList == 0 or paymentList == 0: #if either list..
        return None #..not given, then returns none
    else: #if both are given...
        for x in range(len(namesList)): #for each name index
            lst = [] #starts sublist
            lst.append(namesList[x]) #adds name to sublist
            for y in range(len(paymentList[x])):  #for each payment
                lst.append(paymentList[x][y]) #adds payment w name
            totalList.append(lst) #adds the sublist to overall list
    return totalList #returns the list w everything


def eligibility(*args): 
    result = [] #stores the results to return later
    if type(args[0]) == dict: #if args is a dict
        result = fullCoverageClearance(args[0]) #runs through fCC
    elif type(args) == list or type(args) == tuple: 
        if len(args) > 1: #if there are multiple args
            i = args[0] #first is i, which is namesList
            o = args[1] #second (@index 1) is paymentList
            x = createNewCoverageList(i, o) #runs and stores in x
            y = buildCoverageDictionary(x) #stores results of bCD in y
            result = fullCoverageClearance(y) #stores final in result
        elif len(args) == 1: #if only one arg
            i = buildCoverageDictionary(args[0]) #runs thru, stores in i
            result = fullCoverageClearance(i) #stores in result
    return result #returns the results list with booleans
