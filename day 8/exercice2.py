
def calculate_love_score(n1, n2):
    ar1 = []
    ar2 = []

    for c in n1.upper():
        ar1.append(c)
    for c in n2.upper():
        ar2.append(c)
    suma = 0
    suma2 = 0
    for c in "TRUE":
        counta = ar1.count(c)+ar2.count(c)
        #print(f"{c} occurs {counta} time",end="")
        suma += counta
        if (counta == 1):
            #print("")
            pass
        else:
            #print("s")
            pass
    #print(f"Total = {suma}")
    
    for c in "LOVE":
        counta = ar1.count(c)+ar2.count(c)
        #print(f"{c} occurs {counta} time",end="")
        suma2 += counta
        if (counta == 1):
            #print("")
            pass
        else:
            #print("s")
            pass
    #print(f"Total = {suma2}")
    #print("")
    print(f"{int(str(suma) + str(suma2))}")
       
calculate_love_score("Kanye West", "Kim Kardashian")
