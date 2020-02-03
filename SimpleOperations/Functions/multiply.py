#multiply all numbers in a list
def multiply(nums):
	total = 1
	for number in nums:
		total *= number
	return total

print(multiply([1,2,3,-4]))
