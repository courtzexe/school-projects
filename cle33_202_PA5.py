#-------------------------------------------------------------------------------
# Name: Courtney Le
# Programming Assignment 5
# Due Date: 04/04/2022
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


def increment_attendance(seating, locations):
	for locs in locations: #for each set in locations
		for seating_index in range(len(seating)): #go thru index for seating
			if locs[0] == seating_index: #if the first val is same
				for seats_index in range(len(seating[seating_index])):
					if locs[1] == seats_index: #if second val is same
						seating[seating_index][seats_index] += 1 #adds 1


def drop_lowest(scores, drop_number):
	for num in range(len(drop_number)): #num is index of dropnum
		for i in range(drop_number[num]): #i is iterations 
			for lists in range(len(scores)): #lists is index of scores
				if lists == num: #when index of dropnum and scores same
					lowest = scores[lists][0] #lowest starts at first val
					for score in scores[lists]: #goes through scores
						if score < lowest: #compares scores
							lowest = score #sets lowest sc. as lowest
					scores[lists].remove(lowest) #takes out the lowest


def organize_grades(grades, assignment_types, max_possible):
	book = {'zy':[], 'lab':[], 'pa':[], 'mid1':[], 'mid2':[], 'final':[]}
	for index in range(len(grades)): #goes through indexes of grades
		grade = grades[index] / max_possible[index] #calcs grade
		for aIndex in range(len(assignment_types)): #atype index
			if aIndex == index: #finds when both indexes are same
				book[assignment_types[aIndex]].append(grade) #appends
	return book #appends the corresp. atype with grade into book dict


def gbook_averages(gbook):
	new = {} #new dict with averages
	for key in gbook: #for each assignment type (the key) in gbook 
		grade = gbook[key] #stores the grades into a grades list
		count = 0 #initializes count
		sum = 0 #initializes sum
		for grades in grade: #for each grade in grades list
			sum += grades #sums up all the grades together
			count += 1 #counts how many grades there are
		if count == 0: #if there are no grades then..
			avg_grade = 0 #the average grade is set as 0 
		else: #if there are grades
			avg_grade = sum / count #calculates average of grade
		new[key] = avg_grade #stores the average into the new dict
	return new #returns the new dictionary with averages


def course_grade(gbook, weights, replace):
	cgrade = {} #creates a new dict
	finalgrade = 0 #initializes
	for key in replace: #going through each key in replace
		for gKey in gbook: #going through keys of gbook
			if key == gKey: #finding when both keys are the same
				for g in gbook: #finding when assignment is..
					if g == replace[key]: #same as val in replace
						if gbook[g] < gbook[gKey]: #if less than
							gbook[g] = gbook[gKey] #will replace grade
	for aTypeKey in weights: #assignment types in weights
		weightedg = weights[aTypeKey] * gbook[aTypeKey] #applies weight to g
		cgrade[aTypeKey] = weightedg #adds new weight grades to dict
	for typeKey in cgrade: #goes through each of the grades
		finalgrade += cgrade[typeKey]  #adds grades all together
	return finalgrade
