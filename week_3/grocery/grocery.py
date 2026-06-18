def main():
    lista = {
}
    while True:
        try:
            fruits = input("")

            if fruits in lista:
                lista[fruits] = lista[fruits] + 1

            else:
                lista[fruits] = 1


        except EOFError:
            break

    for fruits in sorted(lista):
        print(lista[fruits] , fruits.upper())




main()

