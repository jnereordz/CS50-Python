import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
        break

    except ValueError:
        pass

randnumber = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            raise ValueError

        if guess == randnumber:
            print("Just right!")
            break
        elif guess < randnumber:
            print("Too small!")
            continue
        else:
            print("Too large!")
            continue

    except ValueError:
        pass
