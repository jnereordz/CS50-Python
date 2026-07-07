import random


def main():
    user_level = get_level()
    score = 0

    for questions in range(10):
        x = generate_integer(user_level)
        y = generate_integer(user_level)
        respuesta = x + y

        for intentar in range(3):
            try:
                intento = int(input(f" {x} + {y} = "))
                if intento == respuesta:
                    score = score + 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {respuesta}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError



if __name__ == "__main__":
    main()
