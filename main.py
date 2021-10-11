# Guessing Game Of Wizard

# Defining variables
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("I am the wizard. Guess the number, puny mortal: "))
    guess_count += 1
    if guess == secret_number:
        print("You won. I am impressed!")
        break
else:
    print("Haha! Mortals can not learn the ways of magic!")