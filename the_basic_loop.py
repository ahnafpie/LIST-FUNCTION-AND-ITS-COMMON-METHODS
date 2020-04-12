# FOR LOOP

monday_temp = [4.5, 6.7, 9.2]  # list

for temp in monday_temp:
    print(round(temp))
' temp is a variable here, which carries out every item of the list through the round function and print it out '

# LOOPING THROUGH A DICTIONARY

std_grades = {"marry": 9.1, "kabir": 3.4, "stiv": 5.6}  # dictionary

for grades in std_grades.values():
    print(grades)

# WHILE LOOP

username = ''

while username != "orbit":
    username = input("Enter UserName: ")

print("We are done! Go to next step")

' For loop ends when its container is exhausted and While loop ends when the condition is false '

# WHILE LOOP WITH BREAK AND CONTINUE

while True:
    name = input("Enter User Name: ")
    if name == 'Git':
        break
    else:
        continue

