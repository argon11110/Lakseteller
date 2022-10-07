trying = True
while trying:
    try:
        laks = int(input("Hvor mange laks er det? "))
        if laks < 1:
            print("Laks må være et heltall større enn 0\n")
        elif laks == 1:
            print(f"{laks} laks")
            if input("Kjør igjen? [j/n]") == "n":
                trying = False
        else:
            print(f"{laks} lakser")
            if input("Kjør igjen? [j/n]") == "n":
                trying = False
    except:
        print("Laks må være et heltall større enn 0\n")