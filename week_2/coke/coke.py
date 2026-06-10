costo = 50
print("Amount due: " , costo)
while costo != 0:
    pagar = input("Inserta Moneda: ")
    if pagar == "10" or pagar == "5" or pagar == "25":
        pagar = int(pagar)
        costo = int(costo - pagar)
        if costo > 0:
            print("Amount Due:", costo)
        else:
            costo = abs(costo)
            print("Change Owed:" , costo)
            break
    else:
         print("Amount Due:" , costo)








