import string
import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = ['!','.','?','!=','#','@',')','(','*','&','%','+','-','/','$',':',';','[',']','{','}','\'','"',]

print(art.logo)
def caesar(direction,message,shift):
	crypted_text = " "
	if direction == 'decode':
		shift *= -1
	for i in message:
		if i.isalpha():
			crypted_index = alphabet.index(i)+shift
			if crypted_index >= 26:
				extra_bits = crypted_index - 26
				crypted_index = extra_bits
			elif crypted_index < 0:
				lower_bits = crypted_index + 26
				crypted_index = lower_bits
			crypted_text += alphabet[crypted_index]
		elif i.isdigit() or i.isspace() or (i in symbols):
			crypted_text += i
	print(f"Here is The {direction}d result : {crypted_text}")

y_or_no = True

while y_or_no:
	direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: \n").lower()
	message = input("Type your message: \n").lower()
	shift = int(input("Type the shift number: \n"))
	caesar(direction,message,shift)
	want_to_continue = input("Type 'yes' if you want to go in again. Otherwise type 'no': \n").lower()
	if want_to_continue == 'yes':
		y_or_no = True
	elif want_to_continue == 'no':
		y_or_no = False
		print("Goodbye!")





