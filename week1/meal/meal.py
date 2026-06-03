


def main():
    comida = input("Que horas son?: ")
    horario = convert(comida)
    if horario >= 7.0 and horario <=8.0:
        print("Breakfast time")
    elif horario >= 12.0 and horario <= 13.0:
        print("Lunch time")
    elif horario >= 18.0 and horario <= 19.0:
        print("Dinner time")
    else:
        pass


def convert(time):
    horas, minutos = time.split(":")
    horas = float(horas)
    minutos = float(minutos)
    minutos = (minutos / 60)
    comida = (horas + minutos)
    return(comida)

if __name__ == "__main__":
    main()







