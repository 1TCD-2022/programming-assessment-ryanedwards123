"""
Filename: Manchester United 22/23 Sqaud    
Author: Ryan Edwards
Date: 26/07/22
Description: Manchester United 22/23 Sqaud for the 22/23 season and the starting lineup and the bench.
"""
#list of all offical players of Manchester United 22/23
Attackers = [ "Cristiano Ronaldo(ST)", "Anthony Martial(ST)", "Marcus Rashford(LM)", "Jadon Sancho(RM)", "Anthony Elanga(LM)", "Tahith Chong(RW)", "Shola Shoretire(RW)", "Alejandro Garnacho(LW)", "Facundo Pellstri(RW)", ]
Midfielders = [ "Bruno Fernandes(CAM)", "Amad(CAM)", "Fred(CM)", "Donny Van De Beek(CM)", "James Garner(CDM)", "Scott Mctominay(CDM)", "Hannibal(CAM)", "Christian Eriksen(CM)"]
Defenders = [ "Victor Lindelof(CB)", "Eric Bailly(CB)", "Phil Jones(CB)", "Harry Maguire(CB)", "Tyrell Malacia(LB)", "Raphael Varane(CB)", "Diogo Dalot(RB)", "Luke Shaw(LB)", "Aaron Wan-Bissaka(RB)",
"Brandon Williams(LB)", "Axel Tuanzehbe(CB)", "Teden Mengi(CB)", "Lisandro Martinez(CB)", ]
Goalkeepers = [ "David De Gea(GK)", "Tom Heaton(GK)"]
VALID_MENU_CHOICE = ["1","2","3","4"]
MENU_USER_CHOICE = ""
Intro = int(input("""\
Welcome to the 22/23 Manchester United Squad!
Firstly you can do these to see our amazing squad for the new season
Type 1 to see attackers
Type 2 to see midfielders
Type 3 to see defenders
Type 4 for goalkeepers

"""))
if Intro == 1:
    list(map(print, Attackers))
if Intro == 2:
     list(map(print, Midfielders))
if Intro == 3:
     list(map(print, Defenders))
if Intro == 4:
    list(map(print, Goalkeepers))







                                    
        

