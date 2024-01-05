#-------------------------------------------------------------------------------
# Name: Courtney Le
# Assignment 2
# Due Date: 02/21/2022
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

# PA2template.py
#using nested for wavelength value
#once value is true, will return the correct spectral color
#when within a certain range, it'll produce the corresponding color
def spectral_color(wavelength):
	if wavelength < 380:
		result = "ultraviolet"	#when less than 380 it is uv
	elif wavelength >= 380 and wavelength <= 449:
		result = "violet"	
	elif wavelength >= 450 and wavelength <= 484:
		result = "blue"
	elif wavelength >= 485 and wavelength <= 499:
		result = "cyan"
	elif wavelength >= 500 and wavelength <= 564:
		result = "green"
	elif wavelength >= 565 and wavelength <= 589:
		result = "yellow"
	elif wavelength >= 590 and wavelength <= 624:
		result = "orange"
	elif wavelength >= 625 and wavelength < 750:
		result = "red"
	elif wavelength >= 750:
		result = "infrared"
	return result

#roomba definition
def robot_actions(side_sensor, front_sensor, dirt_sensor):
	if dirt_sensor == "dirt": #if there is dirt, it'll vacuum
		result = "vacuum"
	elif dirt_sensor == "clear": #if no dirt, will continue through
		if front_sensor == "wall": #no dirt and no wall will make turn
			result = "turn"
		elif front_sensor == "clear": #no dirt, no front can lead to:
			if side_sensor == "wall": #side wall which 
				result = "forward" #will then go forward
			else:					#or will stop if nothing
				result = "stop"
	return result


#first if is if the ticket is hot
#ticket is hot if price rose 50%+ than prev price
#using nested, if ticket fell 50%+ than prev, hold
#anything in between is sell, so uses "else"
def bad_broker(price, prev_price):
	if (prev_price + prev_price * 0.5) <= price: #calc then sees if hot
		result = "BUY"						#will say buy if hot
	elif (prev_price - prev_price * 0.5) >= price: #calc if fell
		result = "HOLD"						#will tell to hold if true
	else:
		result = "SELL"					#will say sell for in between
	return result
