import random
print('''Hello!
    You are in the game, guess the for computer number from 1 to 10.
    Computer have only 3 attempts.''')

ran_number = int(input())
comp_attempts = 0


while comp_attempts <= 3:

    comp_choose = random.randint(1, 10)
    print(comp_choose)


    if comp_choose < ran_number:
        print("Random number is bigger")
        comp_attempts += 1

    if comp_choose > ran_number:
        print("Random number is smaller")
        comp_attempts += 1

    if comp_choose == ran_number:
        comp_attempts -= comp_attempts
        print(f"You are guessed a {ran_number} - random number, in {comp_attempts} attempts.")
        break

    if comp_attempts == 3:
        comp_attempts -= comp_attempts
        print(f"You lose ,{ran_number} - random number")
        break
