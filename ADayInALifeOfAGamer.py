#Name: Akarsh
#Assignment Name: ADayInALife-Gamer.py
#What it does: simulates the life of what the job of an extreme gamers does and allows them to play a quick game
#Submission Date: Nov 12/18

import pygame #using in the program in order to add sounds
import time #time module for time function
import random #random value generator module

print ("-=-=-=-=-=-=-=-=-=-=-=-THE LIFE OF AN EXTREME GAMER-=-=-=-=-=-=-=-=-=-=-=-")

sUserName = input("Enter your name: ")
print ("\n")
print ("Welcome to the glorious life of an extreme gamer, ", sUserName)

sSleep = input("Would you like to wake up. Enter using 'yes' or 'no': ")
if sSleep == "yes":
    sSleep = True 
    print ("Good choice, lets play!")
elif sSleep == "no":
    sSleep = False
    print ("Oh well, we will play games another day!")
    exit()

#instructions for the user
print ("\n")
print ("---------------HOW TO PLAY---------------")
print ("You will get 500 health and 10 power. The")
print ("opponent will be getting their own health")
print ("and deal damage to you. You will get five")
print ("unique moves and will have to destroy the")
print ("opponent within 10 moves because you only")
print ("you only have ten power. Best of luck!!!!")
print ("\n")
time.sleep(5)

print ("The game begins in...")

iCnt = 6 #counter used
for x in range(iCnt):
   iCnt = iCnt - 1
   print (iCnt,"...", end = " ")
   time.sleep(2)
print ("\n")

#variables for the player
iHealth = 500 #users player health
iPower = 10 #users player power
iSwordAttack = 20 #the attack's
iPunch = 10
iDoublePunch = 20
iSpecialPower = 100
iDodge = 0
iODamage = random.randint(50,300)# generates a random number between that range
random.seed()
#all the sound variables
pygame.mixer.init()# to turn on pygame
soundSwords = pygame.mixer.Sound("swords.wav")
soundPunch = pygame.mixer.Sound("punch.wav")
soundSpecialPower = pygame.mixer.Sound("specialpower.wav")
soundDodge = pygame.mixer.Sound("dodge.wav")
soundWin = pygame.mixer.Sound("win.wav")
soundDefeat = pygame.mixer.Sound("defeat.wav")
pygame.mixer.music.load("background.wav")

#The games that the exteme gamer has a chance of playing
iNinjaRun = random.randint (1,100)
if iNinjaRun <= 40:
    time.sleep(2)
    print ("You will be playing the game called Ninja Run")
    pygame.mixer.music.play(-1) #background music plays
elif iNinjaRun <= 60:
    time.sleep(2)
    print ("You will be playing the game called Mortal Kombat X")
    pygame.mixer.music.play(-1)
elif iNinjaRun >= 60:
    time.sleep(2)
    print ("You will be playing the game called Super Mario 2.0")
    pygame.mixer.music.play(-1)

#The opponents the extreme gamer will be versing in the games
if iNinjaRun <= 40:
    print ("Your opponent will be Black Ninja!")
    sEName = ("Black Ninja") #opponent name
    iEHealth = 500 #opponent health
    iODamage = random.randint(50,300) #damage opponent does to users player

elif iNinjaRun <= 60:
    print ("Your opponent will be Skull Fighter!")
    sEName = ("Skull Fighter") #stats for the second opponent
    iEHealth = 100
    iODamage = random.randint(50,300)

elif iNinjaRun >= 60:
    print ("Your opponent will be Mario!")
    sEName = ("Mario") #stats for the third opponent
    iEHealth = 200
    iODamage = random.randint(50,300)

#The game in action
print ("\n")
print (sEName, "would like to verse you!")
print ("\n")
time.sleep(2)
while iHealth > 0 and iEHealth > 0: # this while loop will keep going until the users opponent has been destroyed
    print ("-=-=-=-=-=-=-=-STATS-=-=-=-=-=-=-=-")
    print ("Your Health:", iHealth, "Power:", iPower)
    print (sEName," Health:", iEHealth)
    print ("Your attack choices will be listed below in a moment.")
    time.sleep(3)
    print ("\n")
    print ("Which attack do want do on ",sEName,"?")
    print ("1 - Sword Attack") #diffrent moves for the user
    print ("2 - Punch")
    print ("3 - Double Punch")
    print ("4 - Special Power")
    print ("5 - Dodge")
    iAttack = int(input("Enter the number of the attack chosen: ")) # user can choose which attack they would like to use
    if iAttack == 1:
        iEHealth = iEHealth - iSwordAttack #remaining health for opponent after attack 
        iHealth = iHealth - iODamage #remaining health for users player after attack from opponent
        iPower = iPower - 1 #subtracts one power each move
        pygame.mixer.music.stop() #background music stops
        pygame.mixer.Sound.play(soundSwords) #sound effects
        time.sleep(3)
        pygame.mixer.Sound.stop(soundSwords) #sound effects stop
        pygame.mixer.music.play(-1) #backgroung music plays 
        print ("You deal", iSwordAttack, "to", sEName)
        print (sEName, "does", iODamage, "damage to you")
        print ("You have", iPower, "power remaining")
        time.sleep(2)
        print ("\n")
    elif iAttack == 2:
        iEHealth = iEHealth - iPunch
        iHealth = iHealth - iODamage
        iPower = iPower - 1
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(soundPunch)
        time.sleep(3)
        pygame.mixer.Sound.stop(soundPunch)
        pygame.mixer.music.play(-1)
        print ("You deal", iPunch, "to", sEName)
        print (sEName, "does", iODamage, "damage to you")
        print ("You have", iPower, "power remaining")
        time.sleep(2)
        print ("\n")
    elif iAttack == 3:
        iEHealth = iEHealth - iDoublePunch
        iHealth = iHealth - iODamage
        iPower = iPower - 1
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(soundPunch)
        time.sleep(3)
        pygame.mixer.Sound.stop(soundPunch)
        pygame.mixer.music.play(-1)
        print ("You deal", iDoublePunch, "damage to", sEName)
        print (sEName, "does", iODamage, "damage to you")
        print ("You have", iPower, "power remaining")
        time.sleep(2)
        print ("\n")
    elif iAttack == 4:
        iEHealth = iEHealth - iSpecialPower
        iHealth = iHealth - iODamage
        iPower = iPower - 1
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(soundSpecialPower)
        time.sleep(3)
        pygame.mixer.Sound.stop(soundSpecialPower)
        pygame.mixer.music.play(-1)
        print ("You deal", iSpecialPower, "damage to", sEName)
        print (sEName, "does", iODamage, "damage to you")
        print ("You have", iPower, "power remaining")
        time.sleep(2)
        print ("\n")
    elif iAttack == 5:
        iEHealth = iEHealth - iDodge
        iHealth = iHealth - iODamage
        iPower = iPower - 1
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(soundDodge)
        time.sleep(3)
        pygame.mixer.Sound.stop(soundDodge)
        pygame.mixer.music.play(-1)
        print ("You deal", iDodge, "damage to", sEName)
        print (sEName, "does", iODamage, "damage to you")
        print ("You have", iPower, "power remaining")
        time.sleep(2)
        print ("\n")
    else:
        print ("Oops, looks like you have made the wrong move, ",sEName, "has killed you!")
        time.sleep(2)
        exit() #if the attack is not from the options listed, user will lose and game will be ended

time.sleep(1)

if iPower <= 0: #when player reaches zero power, this will execute
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(soundDefeat)
    print ("You have no more power left!", sEName, "has taken advantage of this and killed you! Better luck next time.")
    time.sleep(4)
    pygame.mixer.Sound.stop(soundDefeat)
    import tkinter as tk #used tkinter to display images if player wins
    root = tk.Tk()
    logo = tk.PhotoImage(file="lose.gif")
    w1 = tk.Label(root, image=logo).pack(side="right")
    explanation = "BETTER LUCK NEXT TIME!"
    w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
    root.mainloop()
    exit()

if iHealth <= 0 and iEHealth > 0: #conditional used if user faces defeat
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(soundDefeat)
    print (sEName, "has defeated you with his jaw breaking moves! Better luck next time.")
    time.sleep(4)
    pygame.mixer.Sound.stop(soundDefeat)
    import tkinter as tk #used tkinter to display images if player wins
    root = tk.Tk()
    logo = tk.PhotoImage(file="lose.gif")
    w1 = tk.Label(root, image=logo).pack(side="right")
    explanation = "BETTER LUCK NEXT TIME!"
    w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
    root.mainloop()
    exit()
elif iEHealth <= 0: #used if user is the winner
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(soundWin)
    print (sEName, "has been defeated successfully, congratulations you have completed the job of a gamer!")
    time.sleep(4)
    pygame.mixer.Sound.stop(soundWin)
    import tkinter as tk #used tkinter to display images if player wins
    root = tk.Tk()
    logo = tk.PhotoImage(file="victory.gif")
    w1 = tk.Label(root, image=logo).pack(side="right")
    explanation = "WINNER!"
    w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
    root.mainloop()
    exit()


