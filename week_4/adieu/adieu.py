import inflect
p = inflect.engine()

nombres = []

while True:
    try:
        name = input("Name: ")
        nombres.append(name)
    except EOFError:
        print("")
        break


print("Adieu, adieu, to" , p.join(nombres))


