import random
from random import uniform
import time
import os
#thanks to everyone on stackoverflow and InvisibleOne and replit
bright_cyan = "\033[0;96m"
bright_red = "\033[0;91m"
green = "\033[0;32m"
bright_blue = "\033[0;94m"
bright_yellow = "\033[0;93m"
purple = '\033[0;95m' 
lives = 125
coins = 13
#lel = random.uniform(0.1, 0.99) 
weapon_damage = 7 #** lel
monsters_killed = 0
#def randuni():
#  while attack == True:
#    weapon_damage = 7 ** lel
#    monsters_killed = 0
#  else: 
#    print(bright_red + "Failed" )

def attack(bright_yellow, bright_blue, green,  bright_red):
  global coins
  global monsters_killed
  global weapon_damage
  global lives
  #global lel
  monster_life = random.randint(1,40)
  monster_damage = random.randint(1,25)
  attacking = True
  while attacking == True:
    os.system('clear')
    print("Lives: " + str(lives))
    print(bright_yellow + "\nYou strike at the monster, it does " + str(weapon_damage) + " damage!!")
    print(bright_red + "\nMonster's health: " + str(monster_life))
    monster_life -= weapon_damage
    print(bright_red + "\nMonster attacks you and does " + str(monster_damage) + " damage!!")
    lives = int(lives)
    lives -= monster_damage
    if lives <= 0:
      time.sleep(1)
      print(bright_red + "\nYou have been defeated...")
      time.sleep(1)
      print(bright_blue + "\nIn your career you killed " + str(monsters_killed) + " monsters")
      time.sleep(2)
      os.system('clear')
      exit()
    elif monster_life <= 0:
      time.sleep(1)
      print(green + "\nYou killed a monster!")
      #coins = int(coins)
      coins += 7
      time.sleep(1)
      print(bright_yellow + "\nYou earned 7 coins!")
      monsters_killed += 1
      os.system('clear')
      break
    else:
      input(bright_red + "\nPress [enter] to continue fighting")
      os.system('clear')
playing = True
while playing == True:
  print(green + "\n[1] Attack")
  print(bright_blue + "\n[2] Upgrade Weapon")
  print(bright_yellow + "\n[3] Coin Balance")
  print(bright_red + "\n[4] Lives")
  print(purple + "\n[5] Buy Lives")
  print(bright_cyan + "") 
  choice = input()
  if choice == '1':
	  attack(bright_yellow, bright_blue, green,  bright_red)
  elif choice == '2':
    if coins >= 7:
      time.sleep(1)
      print(bright_cyan + "\nYou upgraded your weapon!")
      time.sleep(1)
      weapon_damage += 5
      coins -= 7
      print(bright_yellow + "\nSpent 7 coins.")
      time.sleep(1)
      os.system('clear')
    else:
      time.sleep(1)
      print(purple + "\nYou need more coins!!")
      time.sleep(1)
      os.system('clear')
  elif choice == '3':
   coins = int(coins)
   time.sleep(1)
   print(bright_yellow + "\nYou have " + str(coins) + " coins!!")
   time.sleep(1)
   os.system('clear')
  elif choice == '4':
    time.sleep(1)
    print(bright_red + "\nYou have " + str(lives) + " Lives")
    time.sleep(1)
    os.system('clear')
  elif choice == '5':
    if coins <= 10:
      time.sleep(1)
      print(purple + "\nYou need more coins.")
      time.sleep(1)
      os.system('clear')
    else:
      time.sleep(1)
      print(bright_red + "\nYou got another 10 lives!")
      time.sleep(1)
      lives += 10
      coins -= 10
      print(bright_yellow + "\nSpent 10 coins.")
      time.sleep(1)
      os.system('clear')
  else:
   time.sleep(1)
   print(bright_red + "\nHey, that wasn't an option, please choose one or two...")
   time.sleep(1)
   os.system('clear')
