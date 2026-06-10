vocalesm = ["a" , "e" , "i" , "o" , "u"]
vocalesM = ["A" , "E" , "I" , "O" , "U"]

palabra = input("Input: ")
resultado = ""

for remover in palabra:
    if remover in vocalesm:
        resultado = resultado
    elif remover in vocalesM:
        resultado = resultado
    else:
        resultado = resultado + remover

print(resultado)


