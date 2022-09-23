tk="üİçğşöı"


parola = input("parola girin : ")

for i in parola:
    if i in tk:
        raise TypeError("hatalı parola")
    else:
        pass
print("geçerli parola")        




    
