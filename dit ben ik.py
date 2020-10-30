print ("hello you!, ik ben daan.")
print ("voordat de quiz begint even een vraag")
print ("wie ben jij?")
naam = input()
print ("hello " +naam)
print ("er komen 3 vragen antwoord aub met hoofdletters en als je A invult kan dat 1 keer, B moet 2 keer en C moet 3 keer weet niet waarom.")
print ("vraag 1. wat is mijn favoriete game")
print ("A. mario oddesey")
print ("B. smash bros ultimate")
print ("C. mario maker 2")
andwoord = ["A", "B", "C"]
andwoord = input()
vragen = ('oke')
for andwoorden in vragen:
    if andwoord == ("A"):
        print ('fout mijn favoriete game is smash bros ultimate')
        print ('game over')
        break
    elif andwoord == ("B"): 
        print ("correct mijn favoriete game is smash bros ultimate")
    elif andwoord == ("C"):
        print ("fout mijn favoriete game is smash bros ultimate")
        print ('game over')
        break
    else:
        print ("kies een van de opties")
    print ("vraag 2. hoe oud ben ik.")
    print ("A. 15")
    print ("B. 16")
    print ("C. 17")
    andwoord = ["A", "B", "C"]
    andwoord = input()
    if andwoord == ("A"):
        print ('fout ik ben 16')
        print ('game over')
        break
    elif andwoord == ("B"):
        print ('correct ik ben 16')
    elif andwoord == ("C"):
        print ('fout ik ben 16')
        print ('game over')
        break
    else:
        print ("kies een van de opties")
    print ("tot slot vraag 3. welk van deze vakken is het makkenlijkste voor mij.")
    print ("A. Rekenen")
    print ("B. Nederlands")
    print ("C. Engels")
    andwoord = ["A", "B", "C"]
    andwoord = input()
    if andwoord == ("A"):
        print ('correct het is rekenen')
        print ('je had alles goed!')
    elif andwoord == ("B"):
        print ('fout het is rekenen')
        print ('game over')
        break
    elif andwoord == ("C"):
        print ('fout het is rekenen')
        print ('game over')
        break
    else:
        print ("kies een van de opties")
print ("dat was het ik hoop dat je iets over mij hebt geleert")
