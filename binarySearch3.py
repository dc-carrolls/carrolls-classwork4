def binarySearch(aList, itemSought):
		found = False
		index = -1
		first = 0
		last = len(aList)-1
		while first <= last and found == False:
			midpoint = (first + last) div 2
			if aList[midpoint] == itemSought then
				found = 	  		(2)
							  		(3)
			else 	
				if aList[midpoint] < itemSought then
					first = 	      	(4)
				else	
							 		(5)
				endif
			endif
		endwhile
		return index		
		endfunction
