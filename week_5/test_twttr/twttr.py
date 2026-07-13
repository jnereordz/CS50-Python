vocalesm = ["a" , "e" , "i" , "o" , "u"]
vocalesM = ["A" , "E" , "I" , "O" , "U"]

def main():
    palabra = input("Input: ")
    resultado = shorten(palabra)
    print(f"Output: {resultado}")


def shorten(palabra):
    resultado = ""
    for remover in palabra:
        if remover in vocalesm:
            resultado = resultado
        elif remover in vocalesM:
            resultado = resultado
        else:
            resultado = resultado + remover
    return resultado




if __name__ == "__main__":
    main()
