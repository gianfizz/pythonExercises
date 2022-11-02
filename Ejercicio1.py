from time import asctime


def toFloat():
    print(asctime())
    print("Write a number...")
    try:
        personInput = input()
        float(personInput)
        print("Good, you wrote a number")
    except ValueError:
        print("Number required, not letters...")
        return(personInput)
    
toFloat()