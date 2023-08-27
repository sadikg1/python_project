import random

while True:
    print("Enter choice: \n1. Rock \n2. Paper \n3. Scissors \n")
    
    choice = int(input("Your turn: "))
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
        
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
        
    print("Your choice is: " + choice_name)
    print("Computer's turn")
    
    comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
        
    print("Computer's choice is: " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2)or (choice == 3 and comp_choice == 1) or (choice == 2 and comp_choice ==3) ):
        print("Computer Won")
    elif((choice == 2 and comp_choice == 1)or (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice ==2)):
        print("You won!")
    else:
        print("GAME DRAW")
        
    print("Do you want to play again? (Y/N)")
    ans = input()
    
    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
