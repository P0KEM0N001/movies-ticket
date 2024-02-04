"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""
while True:
    try:
        age = input("Enter you age:")
        if age == 'done':
            break
        age = int(age)
        if age < 3 :
            print("your ticket is free.")
        elif age < 12:
            print("your ticket price is $10.")
        elif age < 70:
            print("your ticket price is $15.")
        else:
            print("your ticket is free.")
    except ValueError:
        print("Invalid input. Please enter a number.")



