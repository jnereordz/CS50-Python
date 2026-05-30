def convert(resultado):
    resultado = (resultado.replace( ":)" , "🙂"))
    resultado = (resultado.replace( ":(" , "🙁"))
    return(resultado)


def main():
    resultado = input()
    resultadofinal = convert(resultado)
    print(resultadofinal)


main()




