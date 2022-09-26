# The Declan Digital Experience
import time

declanType = "Undefined"
columbus = False
cleveland = False
cincinnati = False
cornfield = False

def titleCard():
    print("\n\n\n\n\n                                THE DECLAN DIGITAL EXPERIENCE \n==================================================================================================\n\n\n\n\n")

def start():
    print("\n\nChoose Declan Type")
    choice = input("1. Declan \n2. Not an Apple \n3. Big Declan \n4. Entity\n\n")

    if choice == "1":
        declanType = "Declan"
        c1Declan()
    elif choice == "2":
        declanType = "I'm Not an Apple"
        c1Apple()
    elif  choice == "3":
        declanType = "Big Declan"
        bigDeclan()
    elif choice == "4":
        declanType = "Entity"
    elif choice == "23":
        print("\n\nYooo you found the easter egg\n\n")
        time.sleep(5)
        start()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1, 2, 3, or 4)\n\n")
        time.sleep(5)
        start()

def bigDeclan():
    print("\n\nWhat do you want to do")
    choice = input("1. Destroy Ohio\n2. Order a Hotdog\n\n")
    if choice == "1":
        ohio()
    elif choice == "2":
        hotdog()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1, or 2)\n\n")
        time.sleep(5)
        bigDeclan()

def ohio():
    print("\n\nWhat city is first")
    choice = input("1. Columbus\n2. Cleveland\n3. Cincinnati\n4. Cornfield\n\n")
    if  choice == "1" and columbus == False:
        columbusC()
        columbus = True
    elif choice == "2" and cleveland == False:
        clevelandC()
        cleveland = True
    elif choice == "3" and cincinnati == False:
        cincinnatiC()
        cincinnati = True
    elif choice == "4" and cornfield == False:
        cornfieldC()
        cornfield = True
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1, 2, 3, or 4)\n\n")
        time.sleep(5)
        ohio()

def columbusC():
    if columbus == True and cleveland == True and cincinnati == True and cornfield == True:
        ohioGone()
    else:
        print("\n\nWhat city is next")
        choice = input("1. Cleveland\n2. Cincinnati\n3. Cornfield\n\n")
        if  choice == "1" and cleveland == False:
            clevelandC()
            cleveland = True
        elif choice == "2" and cincinnati == False:
            cincinnatiC()
            cincinnati = True
        elif choice == "3" and cornfield == False:
            cornfieldC()
            cornfield = True
        else:
            print("\n\n" + choice + " is an invalid option, please pick a valid option (1, 2, or 3)\n\n")
            time.sleep(5)
            columbusC()

def cornfieldC():
    if columbus == True and cleveland == True and cincinnati == True and cornfield == True:
        ohioGone()
    else:
        print("\n\nWhat city is next")
        choice = input("1. Columbus\n2. Cincinnati\n3. Cleveland\n\n")
        if  choice == "1" and columbus == False:
            columbusC()
            columbus = True
        elif choice == "2" and cincinnati == False:
            cincinnatiC()
            cincinnati = True
        elif choice == "3" and cleveland == False:
            clevelandC()
            cleveland = True
        else:
            print("\n\n" + choice + " is an invalid option, please pick a valid option (1, 2, or 3)\n\n")
            time.sleep(5)
            cornfieldC()

def cincinnatiC():
    if columbus == True and cleveland == True and cincinnati == True and cornfield == True:
        ohioGone()
    else:
        print("\n\nWhat city is next")
        choice = input("1. Columbus\n2. Cincinnati\n3. Cleveland\n\n")
        if  choice == "1" and columbus == False:
            columbusC()
            columbus = True
        elif choice == "2" and cincinnati == False:
            cincinnatiC()
            cincinnati = True
        elif choice == "3" and cornfield == False:
            cornfieldC()
            cornfield = True
        else:
            print("\n\n" + choice + " is an invalid option, please pick a valid option (1, 2, or 3)\n\n")
            time.sleep(5)
            cincinnatiC()

def clevelandC():
    print("\n\nWhat city is next")
    choice = input("1. Columbus\n2. Cincinnati\n3. Cornfield\n\n")
    if  choice == "1" and columbus == False:
        columbusC()
    elif choice == "2" and cincinnati == False:
        cincinnatiC()
    elif choice == "3" and cornfield == False:
        cornfieldC()
    else:
        print("\n\n" + choice + " is an invalid option, please pick a valid option (1, 2, or 3)\n\n")
        time.sleep(5)
        clevelandC()

def c1Declan():
    print("\n\nChoose status")
    choice = input("1. Sick \n2. Going to school \n3. Sleeping\n\n")
    if choice == "1":
        c2DSick()
    elif choice == "2":
        c2DSchool()
    elif choice == "3":
        dSleep()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1, 2, or 3)\n\n")
        time.sleep(5)
        c1Declan()

def c2DSick():
    titleCard()
    print('\n\nEnding 1: Declan has died from a mysterious sickness also known as the "Common Cold"')

def c2DSchool():
    print("\n\nYou went to school and did the schoolwork for that day, what do you want to do when you get home?")
    choice = input("1. Hot Sauce \n2. Gaming \n3. Sleep\n\n")
    if choice == "1":
        c3DHotSauce()
    elif choice == "2":
        c3DGaming()
    elif choice == "3":
        dSleep()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1, 2, or 3)\n\n")
        time.sleep(5)
        c2DSchool()

def dSleep():
    print("\n\nYou fell asleep then woke up\n\n")
    time.sleep(5)
    c1Declan()

def c3DHotSauce():
    titleCard()
    print("\n\nEnding 2: Declan has had too much hot sauce and drowns\n\n")

def c3DGaming():
    print("\n\nWhat do you want to do")
    choice = input("1. Gaming alone \n2. Gaming with the boys\n\n")
    if choice == "1":
        c4DGamingAlone()
    elif choice == "2":
        c4DTHEBOYS()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c3DGaming()

def c4DGamingAlone():
    print("\n\nHow long will you be gaming")
    choice = input("1. Yes (no sleep) \n2. Until 1AM\n\n")
    if choice == "1":
        c1Declan()
    elif choice == "2":
        dSleep()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c4DGamingAlone()

def c4DTHEBOYS():
    titleCard()
    print("\n\nEnding 3: You were gaming with the boys all night and had a good time\n\n")

def c1Apple():
    print("\n\nWhat do you want to do today")
    choice = input("1. Gaming\n2.Make a video\n\n")
    if choice == "1":
        c2AGaming()
    elif choice == "2":
        applevid()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c1Apple()

def applevid():
    print("\n\nWhat video do you want to make")
    choice = input("1. Hitting my desk\n2. Funny mic man eats a burrito\n3. Cocobama\n\n")
    if choice == "1":
        desk()
    elif choice == "2":
        burrito()
    elif choice == "3":
        cocobama()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c2AGaming()

def desk():
    print("\n\nEnding 16: Hitting my desk posted")

def burrito():
    print("\n\nEnding 17: Funny mic man eats a burrito posted")

def cocobama():
    print("\n\nEnding 18: Cocobama posted")

def c2AGaming():
    print("\n\nWhat do you want to do")
    choice = input("1. Gaming alone\n2. Gaming with the boys\n3. Albania\n\n")
    if choice == "1":
        c3AAloneChoose()
    elif choice == "2":
        c3ATheBoys()
    elif choice == "3":
        albania()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c2AGaming()

def c3AAloneChoose():
    print("\n\nWhat game do you want to play")
    choice = input("1. Hearts of Iron IV\n2. CS:GO\n3. Roblox\n4. Minecraft\n\n")
    if choice == "1":
        albania()
    elif choice == "2":
        aloneCSGO()
    elif choice == "3":
        aloneRoblox()
    elif choice == "4":
        aloneMC()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c3AAloneChoose()

def c3ATheBoys():
    print("\n\nWho do you want to hang out with")
    choice = input("1. The Dictableship\n2. Bungers\n3. Kowalski's Server\n\n")
    if choice == "1":
        dictableship()
    elif choice == "2":
        bunger()
    elif choice == "3":
        kowalski()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        c3ATheBoys()

def bunger():
    print("\n\nWhat game will you play")
    choice = input("1. Minecraft\n2. CS:GO\n3. Jackbox\n\n")
    if choice == "1":
        bungerMC()
    elif choice == "2":
        bungerCS()
    elif choice == "3":
        bungerJabox()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        bunger()

def bungerMC():
    titleCard()
    print("\n\nEnding 9: You played Minecraft with the boys in the bunger server all night and had a good time")

def bungerCS():
    titleCard()
    print("\n\nEnding 10: You played CS:GO with the boys in the bunger server all night and had a good time")

def bungerJabox():
    titleCard()
    print("\n\nEnding 11: You played Jackbox with the boys in the bunger server all night and had a good time")

def kowalski():
    print("\n\nWhat game will you play")
    choice = input("1. Minecraft\n2. CS:GO\n\n")
    if choice == "1":
        kowalMC()
    elif choice == "2":
        kowalCS()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        bunger()

def kowalMC():
    titleCard()
    print("\n\nEnding 13: You played Minecraft with the boys in the bunger server all night and had a good time")

def kowalCS():
    titleCard()
    print("\n\nEnding 12: You played CS:GO with the boys in the bunger server all night and had a good time")

def dictableship():
    print("\n\nWhat game will you play")
    choice = input("1. Minecraft\n2. Jackbox\n\n")
    if choice == "1":
        tableMC()
    elif choice == "2":
        tableJackbox()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        bunger()

def tableMC():
    titleCard()
    print("\n\nEnding 15: You played Minecraft with the boys in the bunger server all night and had a good time")

def tableJackbox():
    titleCard()
    print("\n\nEnding 14: You played Jackbox with the boys in the bunger server all night and had a good time")

def aloneCSGO():
    print("\n\nYou got a call from one of the boys do you")
    choice = input("1. Join them\n2. Continue to play alone\n\n")
    if choice == "1":
        csgo()
    elif choice == "2":
        csgo2()
    else:
        print("\n\n" + choice + " is not an option, please pick a valid option (1 or 2)\n\n")
        time.sleep(5)
        aloneCSGO()

def aloneRoblox():
    titleCard()
    print("\n\nEnding 7: You played Roblox alone all night and had a good time")

def aloneMC():
    titleCard()
    print("\n\nEnding 8: You played Minecraft alone all night and had a good time")

def csgo2():
    titleCard()
    print("\n\nEning 6: You played CS:GO alone all night and had a good time")

def csgo():
    titleCard()
    print("\n\nEnding 5: You played CS:GO with the boys all night and had a good time")

def ohioGone():
    titleCard()
    print("\n\nEnding 18: Ohio has been destroyed")

def albania():
    titleCard()
    print("\n\nEnding 4: You became the dictator of Albania, taking over Montenegro, Serbia, Kosovo, North Macedonia, Greece, and Bulgaria. Because you hate Bulgaria you decide to set the entire country on fire and the eyes of the world are watching you.\n\n")

titleCard()
start()