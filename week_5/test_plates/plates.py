def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(character):
    if len(character) >= 2 and len(character) <=  6:
        if character[0].isalpha() and character[1].isalpha():
            numeros = False
            for letras in character:
                if not letras.isalnum():
                    return False
                if letras.isdigit():
                    if numeros == False:
                        if letras == "0":
                            return False
                        numeros = True

                elif letras.isalpha() and numeros:
                    return False


            return True
        return False



    else:
        return False





if __name__ == "__main__":
    main()
