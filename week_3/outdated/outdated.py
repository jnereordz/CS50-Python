meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            fecha = input("Date: ")
            fecha = fecha.strip()
            if "/" in fecha:
                mes , dia , año = fecha.split("/")
                dia = dia.zfill(2)
                mes = mes.zfill(2)
                if mes > "12" or dia > "31":
                    continue

                fecha = (año + "-" + mes + "-" + dia)
                print(fecha)
                break


            else:
                if "," not in fecha:
                    continue
                mes, dia, año = fecha.split(" ")
                dia = (dia.replace(",", ""))
                dia = dia.zfill(2)
                mes = meses.index(mes) + 1
                mes = str(mes)
                mes = mes.zfill(2).replace(" ", "")
                if mes > "12" or dia > "31":
                    continue

                fecha = (año + "-" + mes + "-" + dia)

                print(fecha)
                break


        except ValueError:
            continue










main()
