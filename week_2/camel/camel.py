camel = input("camelCase: ")
resultado = ""

for letras in camel:
    if letras.isupper():
        letras = letras.lower()
        letras = ("_") + letras
        resultado = resultado + letras
    else:
        resultado = resultado + letras

print(resultado)
