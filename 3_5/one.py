nums = []

def analyze_numbers(nums):
	count= 0
	total = 0
	maxi  = None
	
	for num in nums:
		if isinstance(num,(int,float)):
			count += 1
			total += num
			if maxi == None or num > maxi:
				maxi = num
			
	
	average = total / count if count>0 else None
		
	ana_dict = {
				"count":count, 
				"sum":total,
				"average": average,
				"max": maxi,
		
		}
		
	return ana_dict
		
		
print(analyze_numbers(nums))
