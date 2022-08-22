"""
Filename: Manchester United 22/23 Sqaud    
Author: Ryan Edwards
Date: 26/07/22
Description: Manchester United 22/23 Sqaud for the 22/23 season and the starting lineup and the bench.
"""
#list of all offical players of Manchester United 22/23
import sys
import time
Attackers = [ "Cristiano Ronaldo", "Anthony Martial", "Marcus Rashford", "Jadon Sancho", "Anthony Elanga", "Tahith Chong", "Shola Shoretire", "Alejandro Garnacho", "Facundo Pellstri", ]
Midfielders = [ "Bruno Fernandes", "Amad", "Fred", "Donny Van De Beek", "James Garner", "Scott Mctominay", "Hannibal", "Christian Eriksen"]
Defenders = [ "Victor Lindelof""Eric Bailly", "Phil Jones", "Harry Maguire", "Tyrell Malacia", "Raphael Varane", "Diogo Dalot", "Luke Shaw", "Aaron Wan-Bissaka",
"Brandon Williams", "Axel Tuanzehbe", "Teden Mengi", "Lisandro Martinez", ]
Goalkeepers = [ "David De Gea", "Tom Heaton"]
VALID_MENU_CHOICE = ["1","2","3","4","5"]
QUESTION = ["1","2"]
MENU_USER_CHOICE = 0
STARTING_LINEUP_CHOICE = []
menu_repeat = True



while menu_repeat == True: 
     MENU_USER_CHOICE = input("""\
                    Welcome to the 22/23 Manchester United Squad!
                    Firstly you can do these to see
                    our amazing squad for the new season
                    Type 1 to see attackers
                    Type 2 to see midfielders
                    Type 3 to see defenders
                    Type 4 for goalkeepers
                    Type 5 to choose your starting lineup
                    Type 6 to Exit Programm!""")
     while not MENU_USER_CHOICE in VALID_MENU_CHOICE:
          MENU_USER_CHOICE = input("please select a valid option")

     if MENU_USER_CHOICE == "1":
          list(map(print, Attackers))
     elif MENU_USER_CHOICE == "2":
          list(map(print, Midfielders))
     elif MENU_USER_CHOICE == "3":
          list(map(print, Defenders))
     elif MENU_USER_CHOICE == "4":
          list(map(print, Goalkeepers))
     elif  MENU_USER_CHOICE == "5":
          menu_repeat = False
          print("Welcome to create your own starting lineup for the 22/23 season")
          time.sleep(1)
          print("Firstly pick your goalkeeper (GK).")
          list(map(print, Goalkeepers))
          LINEUP = input("Once you have choosen, type the player name:")
          if LINEUP not in Goalkeepers:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          STARTING_LINEUP_CHOICE.append(LINEUP)
          print(STARTING_LINEUP_CHOICE)

          print("Now choose a center back (CB).")
          list(map(print, Defenders))
          LINEUP_2 = input("Once you have choosen, type the player name:")
          if LINEUP not in Defenders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_2)
          print(STARTING_LINEUP_CHOICE)
     

          print("Now choose another center back (CB).")
          list(map(print, Defenders))
          LINEUP_3 = input("Once you have choosen, type the player name:")
          if LINEUP not in Defenders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_3)
          print(STARTING_LINEUP_CHOICE)
    

          print("Now choose a Left back (LB).")
          list(map(print, Defenders))
          LINEUP_4 = input("Once you have choosen, type the player name:")
          if LINEUP not in Defenders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_4)
          print(STARTING_LINEUP_CHOICE)
    

          print("Now choose a right back (RB).")
          list(map(print, Defenders))
          LINEUP_5 = input("Once you have choosen, type the player name:")
          if LINEUP not in Defenders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_5)
          print(STARTING_LINEUP_CHOICE)
     

          print("Now choose a center midfielder (CM).")
          list(map(print, Midfielders))
          LINEUP_6 = input("Once you have choosen, type the player name:")
          if LINEUP not in Midfielders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_6)
          print(STARTING_LINEUP_CHOICE)


          print("Now choose a center midfielder (CM).")
          list(map(print, Midfielders))
          LINEUP_7 = input("Once you have choosen, type the player name:")
          if LINEUP not in Midfielders:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_6)
          print(STARTING_LINEUP_CHOICE)

          
          print("Now choose a Right midfielder or Right Winger (RM,RW).")
          list(map(print, Attackers))
          LINEUP_7 = input("Once you have choosen, type the player name:")
          if LINEUP not in Attackers:
               LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")
          time.sleep(1)
          STARTING_LINEUP_CHOICE.append(LINEUP_6)
          print(STARTING_LINEUP_CHOICE)
"""while LINEUP not in Goalkeepers: LINEUP = input("Please make sure you type there name perfectly! Also only choose from the options given!")  """

































































     







                                    
        

