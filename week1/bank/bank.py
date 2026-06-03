def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip()
    letters(greeting)

def letters(h):
    if h.startswith("hello") or h.startswith("Hello"):
        print("$0")
    elif h.startswith("H") or h.startswith("h"):
        print("$20")
    else:
        print("$100")



main()

