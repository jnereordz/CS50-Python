def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <=  6:
        if s[0].isalpha() and s[1].isalpha():
            numeros = False
            for letras in s:
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




    else:
        return False





main()
