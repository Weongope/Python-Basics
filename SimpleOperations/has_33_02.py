def has_33():
	for i in range(0,len(nums)-1):
		if nums[i:i+2] == [3,3]:
			return True
	
	return False

has_33([3,3,2,1,3,2])