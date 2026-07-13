def main():
        while True:
            fraction = (input("Fraction: "))
            try:
                fraction = convert(fraction)
                print(gauge(fraction))
                break
            except (ValueError, ZeroDivisionError):
                pass



def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
    except (ValueError, ZeroDivisionError):
        raise ValueError


    if y == 0:
        raise ZeroDivisionError

    elif x > y or  x < 0:
        raise ValueError()

    porcentaje = (x / y ) * 100
    return int(round(porcentaje))




def gauge(porcentaje):
     if porcentaje < 2:
        return ("E")
     elif porcentaje > 98:
        return ("F")
     else:
         return (f"{porcentaje}%")




if __name__ == "__main__":
    main()
