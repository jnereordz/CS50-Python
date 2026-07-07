from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=sys.argv[2])
        except Exception:
            sys.exit("Invalid Usage")
        palabra = input("Input: ")
        print("Output:")
        print(figlet.renderText(palabra))
    else:
        sys.exit("Invalid Usage")

elif len(sys.argv) == 1:
    palabra = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print("Output:")
    print(figlet.renderText(palabra))

else:
    sys.exit("Invalid Usage")
