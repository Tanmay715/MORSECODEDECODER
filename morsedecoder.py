# Python program to implement Morse Code Translator 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

# This is the Function to encrypt the string 
def encrypt(message): 
	cipher = ''         #'cipher' -> 'stores the morse translated form of the english string'
	for letter in message: 
		if letter != ' ': 

			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
		
			cipher += ' '

	return cipher 

# Function to decrypt the string i.e From morse code to English
def decrypt(message): 


	message += ' '       #'message' -> 'stores the string to be encoded or decoded' 

	decipher = ''        #'decipher' -> 'stores the english translated form of the morse string' 
	citext = ''          #'citext' -> 'stores morse code of a single character' 
	for letter in message: 

	
		if (letter != ' '): 

		
			i = 0

			citext += letter 

		else: 
			i += 1

			if i == 2 : 

				decipher += ' '
			else: 

				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 

def main(): 
	message = input("ENTER THE MESSAGE TO ENCRYPT : ")
	result = encrypt(message.upper()) 
	print ("ENCRYPTED MESSAGE IN MORSE CODE IS  : " + result) 

	message = "--. . . -.- ... -....- ..-. --- .-. -"
	result = decrypt(message) 
	print ("DECRYPTED MESSAGE IN ENGLISH IS : "+ result) 

if __name__ == '__main__': 
	main() 
