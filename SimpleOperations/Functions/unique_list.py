def unique_list(lst):
	uniquelist =[]
	for element in lst:
		if element not in uniquelist:
			uniquelist.append(element)
	return uniquelist

print(unique_list([1,2,3,4,4,4,4,1,2,3,6,5]))
