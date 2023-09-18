# Function to convert decimal number
def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

	dec_val = 24
	
	# Calling function
	DecimalToBinary(dec_val)
