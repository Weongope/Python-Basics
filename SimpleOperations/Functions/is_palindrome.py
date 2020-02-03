def palindrome(s):
	current_string = ""

	for letter in s.lower():
		if letter.isalpha():
			current_string += letter

	rev_string = current_string[::-1]
	return rev_string == current_string

print(palindrome("Nurses run"))
