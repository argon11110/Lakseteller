trying = True
while trying:
    try:
        laks = int(input("Hvor mange laks er det? "))
        if laks < 1:
            print("Laks må være et heltall større enn 0\n")
        elif laks == 1:
            print(f"{laks} laks")
            trying = False
        else:
            print(f"{laks} laks")
            trying = False
    except:
        print("Laks må være et heltall større enn 0\n")