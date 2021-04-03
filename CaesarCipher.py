
text = "HarshBrahmxatriya"
s = 4
#print("Enter key")
#s = input()
#s = int(s)

def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if(char.isupper()):
			result += chr((ord(char) + s - 65) %26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result

def decrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if(char.isupper()):
			result += chr((ord(char) - s + 65) %26 + 65)
		else:
			result += chr((ord(char) - s + 97) % 26 + 97)
	return result

print("Plain text:"+ text)
print("Shift pattern:"+ str(s))
print("Cipher text:" + encrypt(text,s))
#print("Decrypted Plain text"+ decrypt(text,s))