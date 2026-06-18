menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    costF = 0
    while True:
        try:
            costo = (input("Item: ")).title()
        except EOFError:
            print()
            break
        if costo in menu:
            price = float(menu.get(costo))
            costF = .00 + (costF + price)
            print(f"Total: ${costF:.2f}")


main()
