palavra = str(input("digite uma palavra:")).lower()
tem_a_letra_a = False



for letra in palavra:
     if letra == "a":
       tem_a_letra_a = True
      
    
     if tem_a_letra_a == True:
        print(f"Sua palavra possui a letra A ")
else:
        print("Sua palavra não possui a letra A")