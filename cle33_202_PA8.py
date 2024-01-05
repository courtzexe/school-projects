#-------------------------------------------------------------------------------
# Name: Courtney Le
# Programming Assignment 8
# Due Date: 04/25/2022
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

def read_grades_file(filename, project=False):
	grades = {} #dictionary of student & their grades
	file = open(filename, "r") #opens the file
	lineCount = 0 #keeps track of what line in file
	for line in file: #for each line of the file
		line2 = line.split(",") #splits each thing to be list
		for thing in range(len(line2)): #takes each stat/data
			line2[thing] = line2[thing].strip() #strips whitespace
		if lineCount == 0: #aka: if it's the first line
			grades[line2[0]] = line2[1] #put name into dict
		elif lineCount >= 4: 
			grades[line2[0]] = float(line2[1])
		else:
			key = line2[0] #name of assignment is set as dict key
			l = [] #list of grades for each assignment
			for nums in range(1, len(line2)): #goes through grades
				l.append(float(line2[nums])) #puts the grades into list
			grades[key] = l #stores all in dict
		lineCount += 1 #continues to track what line in file
	if project == False: #if false
		return grades #returns dict as is
	else: #if project is true
		list1 = "pa", "lab", "zy" #list of assignments
		list2 = 9, 11, 15 #parallel list of needed num of assign.
		for ind in range(len(list1)): #for each assignment in list
			sum = 0 #initializes sum
			dictKey = grades[list1[ind]] #the grade val of each assign.
			if len(dictKey) != list2[ind]: #if it is less than needed num
				n = len(dictKey) #stores current num of assignments as n
				for g in dictKey: #for each val of the grades
					sum += float(g) #adds all grades together
				average = sum/n #averages grades
				l = dictKey #stores into a list
				numAppend = list2[ind] - n #num of times needs to append
				while numAppend > 0: #while that val is >0
					l.append(average) #appends average into list
					numAppend -= 1 #subtracs total num of times needs to
				dictKey = l #stores final list back into dict
	return grades #returns dictionary of grades


def write_grades_file(filename, gbook):
	file = open(filename, "w") #creates a file to write in
	for key in gbook: #for every key in gbook dict
		if key != "name": #if the key is not name
			file.write("\n") #creates a new line (so every line after 1st)
		file.write(key + (", ")) #adds to file the key
		other = (gbook[key]) #assigns key's values to "other"
		if type(other) == str: #if its just a string (one val)
			file.write(other) #add to file
		elif type(other) == float: #if it's a float (one val)
			file.write(str(other)) #writes in file
		else: #if its more than one value (a list)
			for i in range(len(other)): #goes through list indexes
				if i < (len(other)-1): #if it is not last value in list
					file.write(str(other[i]) + (", ")) #writes and adds ,
				elif i == (len(other)-1): #if last value in list
					file.write(str(other[i])) #writes & no comma added
	file.close() #closes file