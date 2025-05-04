import random

top_of_range = int(input("Type a number: "))

if top_of_range <= 0:
    print("Please type a number larger that 0 next time.")
    quit()



random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess  = int(input("Make a guess: "))
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number!")
        
        
print(f"You got it in {guesses} guesses")
    