import time
vragen = ('vraag')
print ('Malik woont in Syrië, in Syrië is het zo dat als je 17 bent dat je in dienstplicht moet. Hij is 16 dus het volgende jaar moet hij in dienstplicht.')
time.sleep (5)
print ('Gaat Malik vluchten of blijft hij?')
time.sleep (3)
print ('A.	 Malik wilt niet in dienstplicht maar hij accepteert het maar')
print ('B.	 Malik weigert om in dienstplicht te gaan en gaat vluchten')
antwoord = input()
if antwoord == ("A") or ('a'):
    print ('je koos antwoord A')
    print ('Malik gaat rustig door met alles tot hij 17 werd en dus in dienstplicht moest. Daar werd het leven hem erg moeilijk en moest hij elke ochtend vroeg opstaan om te trainen enz. af en toe werd hij ook zwaar gewond maar daar was dat allenmaal erg normaal dus moest hij af en toe zelfs sprinten met een gebroken been. Na een jaar maakt hij de keuze nog één keer om te beslissen of hij blijft of vlucht.')
    time.sleep (3)
    print ('Zal Malik vluchten of blijft hij?')
    time.sleep (5)
    print('A.	Malik weet hoe hard heb is maar hij kiest er toch voor om te blijven anders had hij deze keuze eerder moeten maken’')
    print('B.	Malik wilt niet langer in dienstplicht en besluit om te vluchten')
    antwoord = input()
    if antwoord == ('A') or ('a'):
        print ('je koos antwoord A')
        print ('Malik vind dat hij de keuze dan eerder had moeten maken en besluit dus te blijven. Hij denkt toch dat na een tijdje het allenmaal beter wordt,  maar hij kon niet fouter zijn. Hij kreeg het namelijk alleen maar moeilijker met elke dag een stukje erger tot uiteindelijk dat hij de oorlog in kon. Malik krijgt een simpele keuzen.')
        time.sleep(15)
        print('Blijft Malik nog één jaar trainen en gaat hij het jaar daarna de oorlog in of gaat hij direct de oorlog in maar hij hoeft dan een jaar korter. (let op een van de keuzes woord zijn dood)')
        time.sleep(5)
        print ('A.	Malik blijft nog  een jaar trainen')
        print ('B.	Malik gaat direct de oorlog in')
        antwoord = input()
        if antwoord == ("A") or ("a"):
            print ('je koos antwoord A')
            print ('Malik besluit nog een jaar te trainen en krijgt dus de zelfde soort training voor een tweede keer. Daarbij zit hij dus in een nieuwe groep en met een paar van zijn oude groep omdat hij alles al heeft moeten doorstaan, daardoor deed hij niet echt meer moeite mee en ging na een jaar later veel te zelf verzekerd de oorlog in en bleef hij ook continu op de front linie zelfs op momenten dat iedereen hem vertelde. Dat werd na een maand dus ook zijn dood.')
            time.sleep(20)
            print('einde dood ')
        elif antwoord == ("B") or ("b"):
            print ('je koos antwoord B')
            print ('Buiten alle zenuwen ging Malik direct de oorlog in om er zo snel mogelijk af te kunnen zijn daarbij heeft hij heel veel bijna dood ervaringen gehad, maar na 2 jaar kon hij het allenmaal eindelijk met rust laten. Bij die tijd was hij al 23 en kon hij eindelijk terug naar zijn familie en verder studeren om daarna een goede baan te kunnen krijgen. Na 5 jaar is hij een succesvolle bussinesman met een daar erg bekend bedrijf ook een vriend van in het leger de politiek in gegaan en is na 8 jaar(van hem uit het leger komen) de wet daar aangepast zodat kinderen van 17 jaar niet meer dienstplicht hebben.')
            time.sleep(20)
            print ('einde goed leven in Syrië')
        else:
            print ('kies er een')
    elif antwoord == ('B') or ('b'):
        print ('je koos antwoord B')
        print ('Malik besluit om te gaan vluchten naar Turkije in Turkije komt hij uiteindelijk in een vluchtelingen kamp terecht waar hij het sowieso al beter heeft. Hij kreeg daar alleen erg weinig eten en iedereen zat tegen hem te zeiken omdat hij als hij het niet wou dat hij dan eerder had moeten vluchten. Malik vraagt zich af of het wel een goed idee is om daar te blijven.')
        time.sleep(15)
        print ('Zal Malik blijven of gaat hij toch weg')
        time.sleep(3)
        print ('A.	Malik blijft in Turkije.')
        print ('B.	Malik zoekt een manier om verder te vluchten')
        antwoord = input()
        if antwoord == ("A") or ("a"):
            print ('je koos antwoord A')
            print ('Malik beslist om buiten alles te blijven en wachten tot hij weer terug kan, Toch voelt het niet helemaal goed dat kan misschien komen omdat hij was gevlucht maar ook om door de anderen daar hem continu in elkaar willen slaan. Uit eindelijk werd het wel beter maar natuurlijk niet compleet. Daarom maakt hij weer een keuze')
            time.sleep(15)
            print ('Blijft Malik in het vluchtelingen kamp om te wachten op dat hij weer terug kan keren naar Syrië of probeert hij een leven op te bouwen in Turkije')
            time.sleep(5)
            print ('A.	Malik blijft in het vluchtelingen kamp')
            print ('B.	Malik probeert een leven op te bouwen in Turkije')
            antwoord = input()
            if antwoord == ("A") or ("a"):
                print ('je koos antwoord A')
                print ('Malik blijft in het vluchtelingen kamp om te wachten tot hij weer terug kan keren naar Syrië in de tijd in het vluchtelingen kamp bleef was er daar niet veel verandert, en na 5 jaar kon hij weer terug maar eenmaal terug realiseerde hij zich pas dat het niet zo simpel was. Malik werd meteen aangehouden en moest toen dus 10 jaar in de gevangenis zitten totdat hij er weer uit kon. Na al dat kon hij eindelijk weer na zijn familie en ging hij weer studeren. Hij ging werken bij een klein bedrijf waar hij werkt voor weinig loon. ')
                time.sleep(15)
                print ('einde slecht leven in Syrië')
            elif antwoord == ("B") or ('b'):
                print ('je koos antwoord B')
                print ('Malik gaat weg uit het vluchtelingen kamp en probeert een nieuw leven op te bouwen in Turkije  verbazend genoeg lukte het ook noch. Na het in burgeren had hij meteen een baantje genomen om wat geld te kunnen verdienen voor het kunnen studeren. Na 3 jaar woont hij op zich zelf in een klein appartement met een goeie baan. Tot slot is zijn familie af en toe langs gekomen zodat ze weer contact hebben.')
                time.sleep(15)
                print ('einde leven in Turkije')
            else:
                print ('kies er een')
        elif antwoord == ('B') or ('b'):
            print ('je koos antwoord B')
            print ('Malik kiest zoekt een manier om te vluchten daar bij vind hij uiteindelijk iemand om hem naar Engeland of Nederland te krijgen. De kosten voor die rijzen zijn alleen behoorlijk wat en hoewel hij net genoeg heeft is die naar Nederland even goedkoper maar hij kent ten minsten een beetje Engels en geen Nederlands ')
            time.sleep(15)
            print ('Waar gaat hij heen?')
            time.sleep(1)
            print ('A.	Malik gaat naar Nederland')
            print ('B.	Malik gaat naar Engeland')
            antwoord = input()
            if antwoord == ("A") or ("a"):
                print ('je koos antwoord A')
                print ('Malik kiest er voor om naar Nederland te gaan. De reis naar nederland hoewel korter is alsnog erg lang, ook had hij weinig momenten dat hij even zijn benen kon strekken of naar het toilet te gaan. Toch bleef hij met het doel om naar nederland te komen en daar een nieuw leven te kunnen beginnen of tenminsten kan blijfen tot hij weer terug kon')
                time.sleep(15)
                print ('Wanneer Malik aan komt in schiphol is het voor hem bijna niet te geloven, hij was zo blij dat hij beina vergat dat hij geen nederlands kon. Toen hij tot die realisatie kwam raakte hij in paniek dus ging hij mensen natuurlijk om hulp vragen. Na een tijdje hielp iemand hem om naar een politie bureau te komen en daar werd hij verder geholpen om eindelijk in nederland te wonen')
                time.sleep(15)
                print ('Hij woont nu in nederland. Zijn familie is ook naar nederland verhuist, en zijn erg trots op hoe goed hij nu nederlands kent. Hij i hier dus goed in geburgerd en zegt zelf ook dat hij niet terug wilt naar Syrië.')
                time.sleep(8)
                print ('einde is dit canon?')
            elif antwoord == ('B') or ('b'):
                print ('je koos antwoord B')
                print ('Malik kiest er voor om naar engelland te gaan hij hoopt dat als hij daar heen gaat dat hij het wat makkelijker zal hebben met een nieuw leven opbouwen. Dat hoopt hij omdat hij dus al engels kent maar het enige probleem is dat hij nu wel amper geld heeft. Geld maakt hem nu alleen niet uit hoopt er gewoon te komen en de rest komt later')
                time.sleep(15)
                print ('De reis was behoorlijk moeilijk hij moest namelijk eerst naar nederland om daar dan een trein te nemen om eindelijk in engelland te komen en hoewel de auto reis veel erger was vond hij de trein erger. Hij kreeg namenlijk een ticket voor de trein werd naar de trein toegewezen en verder moest hij het maar zelf uitvogelen.')
                time.sleep(15)
                print ('Toen hij eindelijk aan kwam in engeland was hij erg opgelucht de reis was namelijk over tot hij zich realiseerde dat hij natuurlijk in een ander land was zonder enige kennis behalfe de taal een klein beetje. Naar een tijdje werd hij door iemand naar een politie bureau gewezen en kon hij daar inburgeren. Na dat mocht hij teidelijk met iemand wonen en kon hij geld verdienen om zelf een klein appartementje te renten.')
                time.sleep(15)
                print ('Nu woont hij nog in engeland en hij spreekt de taal nu ook goed. Zijn familie is ook in nederland gaan wonen dus die zijn ook vaak bij elkaar. tot slot heeft hij nu ook een goede baan en plant hij niet om nog terug te gaan naar Syrië')
                time.sleep(10)
                print ('einde leven in Engeland')
            else:
                print ('kies er een')
        else:
            print ('kies er een')
    else:
        print ('kies er een') 
elif antwoord == ("B") or ('b'):
    print ('je koos antwoord B')
    print ('Malik wilt niet in dienstplicht en besluit er daarom om te gaan vluchten. Hij vlucht dan naar libanon naar een vluchtelingen kamp. Het is daar niet slecht maar hij kreeg er wel weinig te eten maar dat was het slechte zo ongeveer wel. Maar hij wil nog steeds ergens anders heen hij voelt zich daar niet goed.')
    time.sleep(15)
    print ('Gaat malik verder of blijft hij in labanon')
    time.sleep(3)
    print ('A.	Malik besluit om verder te gaan')
    print ('B.	Malik besluit om te blijfen')
    antwoord = input()
    if antwoord == ("A") or ("a"):
        print ('je koos antwoord A')
        print ('Malik wilt niet in dienstplicht en besluit er daarom om te gaan vluchten. Hij vlucht dan naar libanon naar een vluchtelingen kamp. Het is daar niet slecht maar hij kreeg er wel weinig te eten maar dat was het slechte zo ongeveer wel. Maar hij wil nog steeds ergens anders heen hij voelt zich daar niet goed.')
        time.sleep(15)
        print ('Gaat malik verder of blijft hij in labanon')
        time.sleep(3)
        print ('A.	Malik besluit om verder te gaan')
        print ('B.	Malik blijft in Libanon')
        antwoord = input()
        if antwoord == ("A") or ("a"):
            print ('je koos antwoord A')
            print ('Malik besluit om verder te gaan dus via connecties kan hij uiteindelijk naar nederland maar daarvoor moet hij eerst naar turkije gaan. Daarom gaat hij snel naar turkije maar naar turkije lopen duurde erg lang en hij begon te overwegen of het wel een goed idee is om naar nederland te gaan al kan hij ook in turkije blijfen')
            time.sleep(15)
            print ('Gaat Malik naar nederland of naar turkije')
            time.sleep(3)
            print ('A.	Malik gaat naar nederland')
            print ('B.	Malik gaat naar turkije')
            antwoord = input()
            if antwoord == ("A") or ("a"):
                print ('je koos antwoord A')
                print ('Malik besluit om gewoon naar Nederland te gaan dus gaat hij naar de gene die hem het land in smokkelt de prijs voor het smokkelen is behoorlijk duur maar hij had wel net aan genoeg.dan moest hij nog een week wachten en dan kon hij gaan.')
                time.sleep(15)
                print ('Na een week wachten kon Malik eindelijk gaan dus hij ging in de auto en ze reden naar Nederland.de reis was zwaar ket duurde namelijk erg lang ook had hij weinig momenten dat hij even zijn benen kon strekken of naar het toilet te gaan. Toch bleef hij met het doel om naar nederland te komen en daar een nieuw leven te kunnen beginnen of tenminsten kan blijfen tot hij weer terug kon.')
                time.sleep(15)
                print ('Wanneer Malik aan komt in schiphol is het voor hem bijna niet te geloven, hij was zo blij dat hij beina vergat dat hij geen nederlands kon. Toen hij tot die realisatie kwam raakte hij in paniek dus ging hij mensen natuurlijk om hulp vragen. Na een tijdje hielp iemand hem om naar een politie bureau te komen en daar werd hij verder geholpen om eindelijk in nederland te wonen')
                time.sleep(15)
                print ('Hij woont nu in nederland. Zijn familie is ook naar nederland verhuist, en zijn erg trots op hoe goed hij nu nederlands kent. Hij i hier dus goed in geburgerd en zegt zelf ook dat hij niet terug wilt naar Syrië.')
                time.sleep(8)
                print ('einde canon')
            elif antwoord == ('B') or ('b'):
                print ('je koos antwoord B')
                print ('Malik besluit om de reis naar Nederland af te kappen en een leven in turkije te starten. verbazend genoeg lukte het ook noch. Na het in burgeren had hij meteen een baantje genomen om wat geld te kunnen verdienen voor het kunnen studeren. Na 3 jaar woont hij op zich zelf in een klein appartement met een goeie baan. Tot slot is zijn familie af en toe langs gekomen zodat ze weer contact hebben.')
                time.sleep(15)
                print ('einde leven in Turkije 2')
            else:
                print ('kies er een')
        elif antwoord == ("B") or ('b'):
            print ('je koos antwoord B')
            print ('Malik besluit om in libanon te blijven het was er namelijk niet zo slecht. Hij hoopt dat hij daarna weer terug kan naar Syrië. In de tijd die hij daar zit heeft hij veel frienden gemaakt en begint hij ook de taal goed te leren en hij begint zig af te vragen of het beter is om gewoon daar te blijfen of om later terug naar Syrië te gaan.')
            time.sleep(15)
            print ('Blijft Malik in Libanon of gaat hij terug')
            print ('A.	Malik blijft')
            print ('B.	Malik gaat terug')
            antwoord = input
        else:
            print ('kies er een')
    elif antwoord == ('B') or ('b'):
        print ('je koos antwoord B')
        print ('Malik besluit om in libanon te blijven het was er namelijk niet zo slecht. Hij hoopt dat hij daarna weer terug kan naar Syrië. In de tijd die hij daar zit heeft hij veel frienden gemaakt en begint hij ook de taal goed te leren en hij begint zig af te vragen of het beter is om gewoon daar te blijfen of om later terug naar Syrië te gaan.')
        time.sleep(15)
        print ('Blijft Malik in Libanon of gaat hij terug')
        time.sleep(3)
        print ('A.	Malik blijft')
        print ('B.	Malik gaat terug')
        antwoord = input()
        if antwoord == ("A") or ("a"):
            print ('je koos antwoord A')
            print ('Malik besluit om te blijven in Libanon en probeert daar een leven te starten hij krijgt hulp van een van de vrijwilligers daar. Na drie weken is hij officieel een inwoner van Libanon.')
            time.sleep(8)
            print ('Hij woont nu alleen in een huurhuis in Libanon. Zijn familie komt ook af en toe van Syrië naar Libanon. Tot slot heeft hij een stabiele baan en een goed inkomen.')
            time.sleep(5)
            print ('einde leven in Libanon')
        elif antwoord == ('B') or ('b'):
            print ('je koos antwoord B')
            print ('Malik besluit om later terug te gaan naar Syrië. Maar eerst moest hij natuurlijk blijven. na 5 jaar kon hij weer terug maar eenmaal terug realiseerde hij zich pas dat het niet zo simpel was. Malik werd meteen aangehouden en moest toen dus 10 jaar in de gevangenis zitten totdat hij er weer uit kon. Na al dat kon hij eindelijk weer na zijn familie en ging hij weer studeren. Hij ging werken bij een klein bedrijf waar hij werkt voor weinig loon.')
            time.sleep(15)
            print ('einde slecht leven in Syrië 2')
        else:
            print ('kies er een')
    else:
        print ('kies er een')
else:
    print ('kies er een')


























