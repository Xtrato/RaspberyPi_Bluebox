import RPi.GPIO as GPIO

row1 = 17
row2 = 24
row3 = 23
row4 = 22
col1 = 27
col2 = 4
col3 = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(row1, GPIO.IN)
GPIO.setup(row2, GPIO.IN)
GPIO.setup(row3, GPIO.IN)
GPIO.setup(row4, GPIO.IN)
GPIO.setup(col1, GPIO.OUT)
GPIO.setup(col2, GPIO.OUT)
GPIO.setup(col3, GPIO.OUT)

def getKeyPress():
	while True:
		GPIO.output(col1, True)
		if GPIO.input(row1) == True:
			return '1'
		elif GPIO.input(row2) == True:
			return '4'
		elif GPIO.input(row3) == True:
			return '7'
		elif GPIO.input(row4) == True:
			return '*'
		GPIO.output(col1, False)
		GPIO.output(col2, True)
		if GPIO.input(row1) == True:
			return '2'
		elif GPIO.input(row2) == True:
			return '5'
		elif GPIO.input(row3) == True:
			return '8'
		elif GPIO.input(row4) == True:
			return '0'
		GPIO.output(col2, False)
		GPIO.output(col3, True)
		if GPIO.input(row1) == True:
			return '3'
		elif GPIO.input(row2) == True:
			return '6'
		elif GPIO.input(row3) == True:
			return '9'
		elif GPIO.input(row4) == True:
			return '#'

while True:
	print getKeyPress()
	GPIO.output(col1, False)
	GPIO.output(col2, False)
	GPIO.output(col3, False)

GPIO.cleanup()
print 'END'