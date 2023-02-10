import time
import random

#Ok future Gleb, heres the plan:
#This series of notes will be the plan for the pokemon sim. Don't make it too complex, keep it simple.
#There are three paths where you can take this-
#1. Make a hash table (pokedex) that gives the user the ability to access the info of pokemon.
#2. Make the encounter system, this means menus, visuals and the fun stuff, although we run into the problem that the info of the pokemon will not be availible, such as catch rate, typing and other factors.
#3. Write out the attack stats, create a visual menu and make a party with your precaught pokemon.

#Figure ASCII Later
#text = open('ASCII Text and Art/text.txt', 'r')
#textRead = text.readlines()

#i = 0
#while(i<4): 
#  print(str(textRead[i]))
#  i += 1
# -------------------------------------------------
#                     Functions
# -------------------------------------------------

#class Player():
global pc, uncaught, caught
pc = []
uncaught = []
caught = []
hidden = []

firstTime = True

f = open("pythonmon.txt")
gametext = f.read()
alllines = gametext.split('\n')
#print(alllines)
lineTwo = str(alllines)
monName = lineTwo.split(',')

for i in range(len(alllines)):
  uncaught.append(monName[1+5*i])

def map():
  width = 10
  height = 21
  grid = []
  slot = "."
  
  for i in range(height):
    row = []
    grid.append(row)
    for i in range(width):
      row.append(slot)

  grid[6][2] = "⌂"
  grid[18][8] = "⌂"

  for i in range(5):
    grid[10+i][1] = "/"
    grid[10+i][2] = "/"
  for i in range(3):
    grid[3+i][6] = "/"
    grid[3+i][7] = "/"
    grid[3+i][8] = "/"

  for i in range(17):
    grid[0+i][4] = "="
    i += 1
  for i in range(8):
    grid[7][1+i] = "="
    i += 1
  for i in range(6):
    grid[17][3+i] = "="
    i += 1

  grid[x][y] = "@"
  
  for i in range(height):
    #print(id(grid[i]))
    print(grid[i])

def home():
  print("\na. Player Card\nb. Pythondex\nc. Help\nd. Gleb's PC\ne. Save")
  menu = input("What would you like to do?")
  if (menu == "a" or "b" or "c" or "d" or "e"):
    if (menu == "a"):
      card()
    if (menu == "b"):
      dex()
    if (menu == "c"):
      help()
    if (menu == "d"):
      computer(pc)
    if (menu == "e"):
      saveGame()

def lab(repeat):
  while(repeat == True):
    print("Welcome to the lab!\nTo get you started on your journey choose one of these three Pythonmon!")
    print("   ⎛⎝(•ⱅ •)⎠⎞   ⊂(Θ ⌒ Θ)⊃   ʕ•́ᴥ•̀ʔ")
    starters = input("1 | 2 | 3\n")
    if(starters == "1" or "2" or "3"):
      if (starters == "1"):
        caught.append(uncaught[4])
        pc.append(uncaught[4])
        uncaught.pop(4)
        repeat = False
      if (starters == "2"):
        caught.append(uncaught[5])
        pc.append(uncaught[5])
        uncaught.pop(5) 
        repeat = False
      if (starters == "3"):
        caught.append(uncaught[6])
        pc.append(uncaught[6])
        uncaught.pop(6) 
        repeat = False
  if(repeat == False):
    print("There is a sign that says they are busy doing research.")

def tallGrass():
  prob = random.randint(1, 100)
  print(prob)
  if (prob <= 60):
    print("common")
    i = random.randint(0,3)
    catch(60, i)
  if (prob > 60 and prob <= 85):
    print("uncommon")
    i = random.randint(4,6)
    catch(80, i)
  if (prob > 85 and prob <= 95):
    print("rare")
    i = random.randint(7,8)
    catch(90, i)
  if (prob > 95 and prob <= 100):
    print("legendary")
    i = 9
    catch(95, i)

def catch(rate, posnum):
  encounter = alllines[posnum].split(",")
  print(encounter[1] + encounter[4])
  choose = input("Attempt to Catch | C or Run Away | R\n")
  if (choose == "C" or "c" or "R" or "r"):
    if (choose == "C" or choose == "c"):
      chances = random.randint(1, 100)
      if (chances > rate):
        time.sleep(1)
        print("Congratulations, you caught " + encounter[1] + "!")
        caught.append(uncaught[posnum])
        pc.append(uncaught[posnum])
        uncaught.pop(posnum)
      else:
        time.sleep(1)
        print("Oh no! It got away!")
    if (choose == "R" or choose == "r"):
      print("You ran away!")
      time.sleep(1)

def computer(list):
  box = str(list)
  print("Box 1:\n" + box)

def help():
  print("\nWelcome to Pythonmon\n The goal of the game is to catch every variety of Pythonmon.\n Every Pythonmon has a rarity determining how often they appear.\n To attempt to catch a Pythonmon interact with the grass.\n The list of every play interaction is below: \n / = grass, ⌂ = buildings\n To search up info on a Pythonmon, look up their name in the dex.\n To see what Pythonmon you have caught, check the PC.\n Happy Hunting!")
def dex():
  class Dex:

      def __init__(self, num, name, typing, rarity, image):
        self.num = num.strip()
        self.name = name.strip()
        self.typing = typing.strip()
        self.rarity = rarity.strip()
        self.image = image
      
      def getKey(self):
        key = self.name
        return key

      def __str__(self):
        return "\n" + "[" + self.num + "]" + "\n" + self.name + "\nType: " + self.typing + "\nRarity: " + self.rarity + "\n" + self.image

      def __repr__(self):
        return self.__str__()

  class HashTable:
    def __init__(self, size):
      self.size = size
      #print(self.size)
      self.mons = []
      for i in range(self.size):
        self.mons.append([])

    def hf(self, key):
      return abs(hash(key)) % self.size

    def insert(self, mon):
      index = self.hf(mon.getKey())
      self.mons[index].append(mon)
      pass

    def lookup(self, key):
      index = self.hf(key)
      result = []
      #none = "This Pythonmon Has Not Been Caught"
      print(self.mons[index])
      for mons in self.mons[index]:
        if key == mons.getKey():
          result.append(mons)
            #print(result)
            #result.pop(none)
        #else:
          #result.append(none)
          #print(result)
      print("_____________ ")
      for mon in result:
        print(mon)
            
  length = len(alllines)
  length = int(length)
  #print(length)
  #print(alllines)
  i = 0
  hashTable = HashTable(length)
  for i in range(length):
      values = alllines[i].split(",")
      mon = Dex(values[0], values[1], values[2], values[3], values[4])
      hashTable.insert(mon) 
  userInput = input("\nWhat Pythonmon would you like to know about?\n")
  providedKey = userInput.replace(" ", "")
  hashTable.lookup(providedKey)

def card():
  total = len(caught)
  total = str(total)
  print("\nName: " + name + " " + gender + "\n" + "Pythonmon Found: " + total + "/10" + "\n")

def saveGame():
  global name, gender, pc, uncaught, caught
  file = open("save.txt", "w")
  for i in pc:
    file.write(str(i)+",")
  file.write("\n")
  for i in caught:
    file.write(str(i)+",")
  file.write("\n")
  for i in uncaught:
    file.write(str(i)+",")
  file.write("\n")
  file.write(name)
  file.write("\n")
  file.write(gender)

def loadGame():
  file = open("save.txt", "r")
  global name, gender, pc, uncaught, caught
  lines = file.readlines()
  final = []
  for i in lines:
    final.append(i.strip())
  
  linespc = final[0].split(",")
  linespc.pop(-1)
  for i in range(len(linespc)):
    finalpc = linespc[i].split(",")
    if (len(finalpc) > 0):
      pc.append(finalpc)

  linescaught = final[1].split(",")
  linescaught.pop(-1)
  for i in range(len(linescaught)):
    finalcaught = linescaught[i].split(",")
    if (len(finalcaught) > 0):
      caught.append(finalcaught)

  linesuncaught = final[2].split(",")
  linesuncaught.pop(-1)
  uncaught.append(linesuncaught)

  name = final[3]
  gender = final[4]
  
  file.close()

  
# -------------------------------------------------
#                   Introduction
# -------------------------------------------------

global gender
mfQuestion = True
confirmation1 = True
gender = ""
saved = True
titleCard = False

title = open('ASCII Text and Art/title.txt', 'r')
titleRead = title.read()
print(titleRead)
loadSave = input("New Game | N / Load Game | L\n")
while(saved == True):
  #if (loadSave == "N", "n", "L", "l"):
  if (loadSave == "N" or loadSave == "n"):
    saved = False
    titleCard = True
  if (loadSave == "L" or loadSave == "l"):
    loadGame()
    x = 6
    y = 2
    confirmation1 = False
    mfQuestion = False
    saved = False
      

if (titleCard == True):
  print("\nHello there! Welcome to the world of Pythonmon! My name is Gleb! \nPeople call me the programmer of this game!\nThis game is inhabited by creatures called Pythonmon! So tell me...")

while(confirmation1 == True):
  while(mfQuestion == True):
    mf = input("\n  Are you a boy or a girl?")
    if(mf == "boy" or mf == "Boy" or mf == "girl" or mf == "Girl"):
      if (mf == "boy" or mf == "Boy"):
        gender = "♂"
        mfQuestion = False
      if (mf == "girl" or mf == "Girl"):
        gender = "♀"
        mfQuestion = False
    else:
      mfQuestion = True
  global name
  name = input("\n  Now tell me. What's your name?")

  print("\n   So you are " + name + " and you are " + gender + " ?")

  confirm1 = input("\n  y/n-  ")
  if (confirm1 == "y" or confirm1 == "n"):
    if(confirm1 == "y"):
      confirmation1 = False
    if(confirm1 == "n"):
      confirmation1 = True
      mfQuestion = True
  else:
    confirmation1 = True

if (titleCard == True):
  print("\nOur very own Pythonmon legend is about to unfold!\nA world of dreams and adventures with Pythonmon awaits!\nLet's go!")

#------------------------------------------------------
#                    Game Start
#------------------------------------------------------

time.sleep(2)
#print("\n ")
forest = open('ASCII Text and Art/forest.txt', 'r')
forestRead = forest.read()
print(forestRead)
#time.sleep(2)
print("\n")
if(titleCard == True):
  x = 7
  y = 2
while True:
  movement = input("w|up s|down a|left d|right e|interact\n")
  if (movement == "w" or "s" or "a" or "d" or "e"):
    if (movement == "s"):
      if (x<20):
        x += 1
    if (movement == "a"):
      if (y>0):
        y -= 1
    if (movement == "d"):
      if (y<9):
        y += 1
    if (movement == "w"):
      if (x>0):
        x -= 1
    if (movement == "e"):
      if (x == 6 and y == 2):
        home()
      if (x == 18 and y == 8):
        lab(firstTime)
        firstTime = False
      #these if statements are highly ineffecient, if I had more time I would redo this system.
      if (x == 10 and y == 1):
        tallGrass()
      if (x == 10 and y == 2):
        tallGrass()
      if (x == 11 and y == 1):
        tallGrass()
      if (x == 11 and y == 2):
        tallGrass()
      if (x == 12 and y == 1):
        tallGrass()
      if (x == 12 and y == 2):
        tallGrass()
      if (x == 13 and y == 1):
        tallGrass()
      if (x == 13 and y == 2):
        tallGrass()
      if (x == 14 and y == 1):
        tallGrass()
      if (x == 14 and y == 2):
        tallGrass()
      if (x == 3 and y == 6):
        tallGrass()
      if (x == 3 and y == 7):
        tallGrass()
      if (x == 3 and y == 8):
        tallGrass()
      if (x == 4 and y == 6):
        tallGrass()
      if (x == 4 and y == 7):
        tallGrass()
      if (x == 4 and y == 8):
        tallGrass()
      if (x == 5 and y == 6):
        tallGrass()
      if (x == 5 and y == 7):
        tallGrass()
      if (x == 5 and y == 8):
        tallGrass()
      
      if (x == (10 or 11 or 12 or 13 or 3 or 4 or 5) and y == (1 or 2 or 6 or 7 or 8)):
        tallGrass()
  map()