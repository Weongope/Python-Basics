def lesser_of_two_evens(a,b):
	if (a % 2 == 0 and b % 2 == 0):
		if a < b:
		    print(a)
		else:
		    print(b)
	else:
	    if a > b:
	        print(a)
	    else:
	        print(b)
        
lesser_of_two_evens(1,7)