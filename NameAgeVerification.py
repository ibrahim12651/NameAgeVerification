from time import sleep
from datetime import date

name = input("Enter your first name: ")
sleep(2)
age = date.today().year - int(input("Enter your year of birth: "))
sleep(2)
print("Your name: " + name + ", your age: " + str(age))
for i in ["Arguments are going to be checked...", "Connecting to the system.....", "Connected successfully."]:
    sleep(2)
    print(i)
sleep(1)
for i in range(5):
    sleep(1)
    print("Checking name in " + str(5-i) + " seconds...")
sleep(3)
print("Successfully checked.")

sleep(1)
if name == "İbrahim" or name == "ibrahim":
    print("Your name is correct!")
else:
    print("The name " + name + " is wrong!")

sleep(1)
for i in range(5):
    sleep(1)
    print("Age will be checked in " + str(5-i) + " seconds...")
sleep(3)
print("Successfully checked!")

if 18 <= age <= 25:
    sleep(1)
    print("You can pass.")
else:
    sleep(1)
    print("You can't get in!")
