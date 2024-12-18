def elsofeladat():
    print("\n 1 feladat.")
    muzeum_neve:str=str(input("Múzeum neve: "))
    latogato_neve:str=str(input("Látogató neve: "))
    ertekeles:int=int(input("1-20: "))


    if (ertekeles < 0):
        print("Az értékelés nem lehet negatív!")
    elif (ertekeles == 0):
        print("Az értékelés nem lehet nulla ")
    elif (ertekeles > 20):
        print("20 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")    
    