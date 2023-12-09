import random
import string
print("------------------PASSWORD GENERATOR----------------")
print("")
length= int(input("Enter the password length: "))
print(" Please select the character set from the given below options:")
print("press 1 for DIGITS")
print("press 2 for ALPABETS")
print("press 3 for SPECIAL CHARACTERS")
print("press 4 for EXTT ")

character_list=""
while(True):
    choice=int(input("choose a number: "))
    if choice==1:
        character_list= string.ascii_letters+character_list
    elif choice == 2:
        character_list= string.digits+character_list
    elif choice ==3:
        character_list= string.punctuation+character_list
    elif choice==4:
        break
    else:
        print("Enter the correct option")
output=""
password =[]

for i in range (length):
    char=random.choice(character_list)
    password.append(char)

for i in password:
    output=output+i

print("The generated password is :", output)