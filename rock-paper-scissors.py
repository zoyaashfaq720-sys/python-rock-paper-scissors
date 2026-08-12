import random

choices = {
        'r' : '🪨',
        'p' : '📃',
        's' : '✂️'
    }

while True:

    user_choice = input("Enter your choice(r,p,s) : ").lower()
    
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice('rps')

    print("You choose : ",choices[user_choice])
    print("Computer choose : ",choices[computer_choice])

    if (user_choice == 'r' and computer_choice == 's' or
        user_choice == 'p' and computer_choice == 'r' or
        user_choice == 's' and computer_choice == 'p' ):
        print("Congrats! you won the game.")
        
    elif user_choice == computer_choice:
        print("Its a tie!")
    else:
        print("You lose!")

    continue_game = input("Do you again wants to play(y/n) : ").lower()
    if continue_game == 'y':
        continue
    else:
        break