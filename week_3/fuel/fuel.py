def main():
    while True:
        fraction = (input("Fraction: "))
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            porcentaje = check(x,y)
            if porcentaje < 2:
                print("E")
            elif porcentaje > 98:
                print("F")
            else:
                print(f"{porcentaje}%")

            break
        
        except (ValueError, ZeroDivisionError):
            pass



def check(x,y):
    if x == y:
        return 100

    elif x > y or  x < 0:
        raise ValueError()

    elif x < y:
        porcentaje = (x / y ) * 100
        return int(round(porcentaje))

    else:
        pass








main()
