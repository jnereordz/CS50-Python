def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip()
    money = value(greeting)
    print(money)


def value(h):
    if h.startswith("hello") or h.startswith("Hello"):
        money =  0
    elif h.startswith("H") or h.startswith("h"):
        money = 20
    else:
        money = 100

    return money


if __name__ == "__main__":
    main()
