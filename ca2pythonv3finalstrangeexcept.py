countMax = 0
countB = 0 
maximum = None
minimum = None
while True:				
	numberIn = raw_input('Enter a postive interger number: ')
	if numberIn == '0':			
		print 'game over'
		break #
	try: 
		numberIn = int(numberIn)
        except:
            print 'enter a number'
		
	if maximum is None and minimum is None:
		maximum = numberIn
		minimum = numberIn
	if numberIn >= maximum:
		maximum = numberIn
		countMax = countMax + 1
	if numberIn <= minimum:
		minimum = numberIn
        countB = countB + 1
                				
		
print 'Count Min:', countB, 
print 'Maximum', maximum, 
print 'Count Max:', countMax
print 'Minimum', minimum


			
			
			
			 		
			
			   
			
			
			
			
			
			
			
			
			
