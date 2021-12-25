import random

user_name = str(input("What is your name?"))

while True:
    # welcomes____________________
    print(f'''Hello {user_name}!
    Welcome to the of Rock Paper Scissors game.
    Your opponent is a Computer\n 
     1 - Rock;
     2 - Paper
     3 - Scissors''')

    # user operation choose____________________
    user_choose = input("Your choose (number): ")

    # user choose area____________________
    if user_choose == "1":
        print("\nYour choose: Rock")

    elif user_choose == "2":
        print("\nYour choose: Paper")

    elif user_choose == "3":
        print("\nYour choose: Scissors")

    # computer operation choose____________________
    computer_random_choose = random.randint(1, 4)

    if computer_random_choose == 1:
        print("\nComputer choose: Rock")

    elif computer_random_choose == 2:
        print("\nComputer choose: Paper")

    elif computer_random_choose == 3:
        print("\nComputer choose: Scissors")

    # user and computer game results

    # user choose == 1 or  rock____________________
    if user_choose == "1" and computer_random_choose == 1:
        print("\nDraw!")

    elif user_choose == "1" and computer_random_choose == 2:
        print("\nComputer has won!!!")

    elif user_choose == "1" and computer_random_choose == 3:
        print(f"\n{user_name} has won!!!")


    # user choose == 2 or  paper____________________
    elif user_choose == "2" and computer_random_choose == 1:
        print(f"\n{user_name} has won!!!")

    elif user_choose == "2" and computer_random_choose == 2:
        print(f"\nDraw!")

    elif user_choose == "2" and computer_random_choose == 3:
        print(f"\nComputer has won!!!")


    # user choose == 3 or  scissors____________________
    elif user_choose == "3" and computer_random_choose == 1:
        print(f"\nComputer has won!!!")

    elif user_choose == "3" and computer_random_choose == 2:
        print(f"\n{user_name} has won!!!")

    elif user_choose == "3" and computer_random_choose == 3:
        print("\nDraw!")


    a = input("\n1 = continue, 2 = quit")
    if a == "1":
        print()
        continue
    else:
        print("Thanks for the game!")
        break
