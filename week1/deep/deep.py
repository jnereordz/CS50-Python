question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
question = question.lower()
question = question.strip()

if question == "42" or question == "forty-two" or question == "forty two":
    print("yes")
else:
    print("no")


