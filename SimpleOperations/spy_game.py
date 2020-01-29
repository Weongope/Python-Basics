def spy_game(nums):
	agent = ""
	for i in range(0, len(nums)):
		if nums[i] == 0 or (nums[i] == 7 and len(agent) > 0):
			agent += str(nums[i])
	return ("007" in agent)

print(spy_game([7, 0, 3, 0, 0, 7, 3, 7]))
