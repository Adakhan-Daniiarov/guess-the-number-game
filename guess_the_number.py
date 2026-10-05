import random


input_valid1 = False

# choosing difficulty for the game

while not input_valid1:
    try:
        difficulty = int(input("""Choose the difficulty:
        easy - 1
        medium - 2
        hard - 3
        :"""))
        if difficulty == 1 or difficulty == 2 or difficulty == 3:
            input_valid1 = True
    except ValueError:
        print("Invalid value. Choose the number of difficulty")
        input_valid1 = False


# set difficulty for the game


def set_difficulty(difficulty: int):
    if difficulty == 1:
        return 50
    elif difficulty == 2:
        return 100
    elif difficulty == 3:
        return 500
difficulty2 = set_difficulty(difficulty)
random_num = random.randint(1,difficulty2)



# guessing process


def guessing_process(guess_num: int, random_num: int) -> None:
    counter = 1
    while guess_num != random_num:
        if guess_num > random_num:
            print("Random number is smaller! Try one more time")
            counter += 1
        elif guess_num < random_num:
            print("Random number is bigger! Try one more time")
            counter += 1
        guess_num = int(input("Your number: "))
    print(f"""Congratulations! The random number was {random_num}.
    Number of attempts: {counter}""")



# playing the game


input_valid = False


while not input_valid:
    try:
        guess_num = int(input("Your number: "))
        input_valid = True
        guessing_process(guess_num, random_num)
    except ValueError:
            input_valid = False
            print("Wrong datatype. Please type the integer")
           
  







