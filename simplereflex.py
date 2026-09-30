def SimpleReflex(left, right, position):
    print("Initial condition")
    print("Right:", right)
    print("Left:", left)
    print("position:", position)

    while left=="dirty" or right=="dirty":
        if position=="left" and left=="dirty":
            print("Clean!!")
            left="Clean"
        elif position=="dirty" and right=="dirty":
            print("Clean!!")
            right="Clean"
        elif position=="left" and right=="dirty":
            print("Move Right!!")
            right="Clean"
        else:
            print("Move Left!!")
            left="Clean"

    print("Final condition")
    print("Right:", right)
    print("Left:", left)
    print("Position:", position)
    print("All are cleaned")

SimpleReflex("dirty","dirty","left")