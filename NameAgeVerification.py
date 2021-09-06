import time

thisyear = 2021 # enter your current Example year thisyear = 2021
 

name = input("What is your name ")
time.sleep(2)
year = int(input("Enter your year of birth: "))
year = thisyear - year
time.sleep(2)
print("Your name:", name, "Your age: ", year)
time.sleep(2)
print("System Check To Be Checked...")
time.sleep(2)
print("Connecting to the System.....")
time.sleep(1)
print("Connected successfully. ")

time.sleep(2)
print("Checking Name 5 seconds..")
time.sleep(1)
print("Checking Name 4 seconds..")
time.sleep(1)
print("Checking Name 3 seconds..")
time.sleep(1)
print("Checking Name 2 seconds..")
time.sleep(1)
print("Checking Name 1 seconds..")
time.sleep(3)
print("Successfully checked.")

if (name=="İbrahim") or (name=="ibrahim"):
    time.sleep(1)
    print("Your Name Is Correct")
else:
    time.sleep(1)
    print("Name Wrong " +name)

time.sleep(2)
print("Age Checking 5 second..")
time.sleep(1)
print("Age Checking 4 second..")
time.sleep(1)
print("Age Checking 3 second..")
time.sleep(1)
print("Age Checking 2 second..")
time.sleep(1)
print("Age Checking 1 second..")
time.sleep(3)
print("Successfully checked..")


if (int(year)>=18 and int(year)<=25):
    time.sleep(1)
    print("You can pass. ")
else:
    time.sleep(1)
    print("You can't get in!. ")
