# import modules
import string
import random
# store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("Enter the number of characters required (not less than 8) ")

while True:
	try:
		characters_number = int(user_input)
		if characters_number < 8:
			print("Your number should be at least 8.")
			user_input = input("Please, Enter your number again: ")
		else:
			break
	except:
		print("Please, Enter numbers only.")
		user_input = input("How many characters do you want in your password? ")

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


p1 = round(characters_number * (30/100))
p2 = round(characters_number * (20/100))

result = []
for x in range(p1):
	result.append(s1[x])
	result.append(s2[x])

for x in range(p2):
	result.append(s3[x])
	result.append(s4[x])

random.shuffle(result) #helps making the password stronger

password = "".join(result)
print("The Strong Password: ", password)
