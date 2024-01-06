#-------------------------------------------------------------------------------
# Name: Courtney
# Programming Assignment 4
# Due Date: 03/14/2022
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def biggest_vertebrate(animals, weights, vertebrates):
    newVertAni = [] #list of just vertebrate animals
    newWeight = [] #list of corresponding weights to newVertAni 
    for a in range(len(animals)): #a is index val of animals
        for v in range(len(vertebrates)): #v = index val of verts
            if animals[a] == vertebrates[v]: #if the animal is a vert
               newVertAni.append(animals[a]) #will add the animal to new list
               newWeight.append(weights[a]) #adds corresponding weight too
    if len(newVertAni) < 1: #checks if list is empty
        max_animal = None #if empty list, there are no verts in animal list
    else: #if list isnt empty then...
        max_weight_loc = 0
        for i in range(len(newWeight)): #goes through index of new weight list
            if newWeight[i] > newWeight[max_weight_loc]: #finds highest weight
                max_weight_loc = i #stores max weight index num
        max_animal = newVertAni[max_weight_loc] #finds corresp. animal 
    result = max_animal #animal with highest weight
    return result


def within_weight(animals, weights, weightLimit):
    newAni = [] #new list with animals that have weight < weightLimit
    for w in range(len(weights)): #cycles through weights
        if weights[w] <= weightLimit: #if weight is less than limit
            newAni.append(animals[w]) #adds the animal with that weight..
    result = newAni #..to the new list
    return result #returns the new list that's under weightLimit


def any_adjacent_vertebrates(animals, vertebrates):
    result = False #initializes, false until proven true
    for a in range(len(animals)): 
        for v in range(len(vertebrates)):
            if animals[a] == vertebrates[v]: #if ani is a vert
                for v in range(len(vertebrates)):
                    if animals[a - 1] == vertebrates[v]: #checks if ani..
                        result = True #..before is a vert
                        break #stops checking once finds vert
                    if ((a + 1) < len(animals)): #making sure in bounds
                        if animals[a + 1] == vertebrates[v]: #checks if..
                            result = True #..the animal after is a vert
                            break #stops checking once true
                    else: #if no verts adjacent
                        result = False #returns false
    return result #returns whether true/false


def count_weights(weight_list):
    sums = [] #list of sums of each num
    count = 0 #initialises
    for x in range(len(weight_list)): #goes through each weight
        for y in (range(len(weight_list))): #goes through weigh to add
            while y > x: #making sure does not repeat weights
                sums.append(weight_list[x] + weight_list[y]) #adds to list
                break #ends while loop so not infinite
    for i in sums: #goes through sums list
        for v in weight_list: #compares sums to weights
            if v == i: #finds if the sum is equal to a weight
                count += 1 #counts how many times the sum == weight
                break #once finds one, doesn't cycle through rest of weights
    result = count #the final total count after going through all sums list
    return result
