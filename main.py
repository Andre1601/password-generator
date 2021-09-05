#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#random letter manual pick up or if you want simple code, you can use random.choice(list)
random_letters = ""
for letter in range(0, nr_letters):
  random_letters += letters[random.randint(0, len(letters)-1)]

#random symbol manual pick up
random_symbols = ""
for symbol in range(0, nr_symbols):
  random_symbols += symbols[random.randint(0, len(symbols)-1)]

#random number manual pick up
random_numbers = ""
for number in range(0, nr_numbers):
  random_numbers += numbers[random.randint(0, len(numbers)-1)]

#the above result must be sum to get string(password)
random_password = random_letters + random_symbols + random_numbers

password_of_list = list(random_password)
length = len(password_of_list)
generate_password = ""

#it must be shuffled to ensure against password crack. if it not, you only have weak password and get result : AAA@@@555
for shuffle in range(0, length):
  rand1 = random.randint(0, length-1)
  rand2 = random.randint(0, length-1)

  # password_of_list[rand1], password_of_list[rand2] = password_of_list[rand2], password_of_list[rand1]

  #or you can use random.shuffle(list) if you want your code look simple
  temp = password_of_list[rand1]
  password_of_list[rand1] = password_of_list[rand2]
  password_of_list[rand2] = temp

for password in password_of_list:
  generate_password += password

print(generate_password)
