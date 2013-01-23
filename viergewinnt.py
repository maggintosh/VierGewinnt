import random

### Bugs to fix:
### full board
### quit game

class game:             # Klasse game mit Reihen, Zeilen und Anzahl der Spieler    
    def __init__(self, rows = "4", columns = "4", players = 1):
        self.rows = rows        # Anzahl Reihen
        self.columns = columns  # Anzahl Spalten
        self.players = players  # Anzahl Spieler

class board:            # Klasse board mit Zellen, Matrix des Spielfeldes und Spielerinput    
    def __init__(self, blank = "|___|", one = "|_X_|", two = "|_O_|", matrix = "", insert = "", full = ""):
        self.blank = blank      # Leere Zelle
        self.one = one          # Zelle Spieler 1
        self.two = two          # Zelle Spieler 2
        self.matrix = martix    # Dictionary mit Zellenwerten
        self.insert = insert    # Spielerinput
        self.full = full

def players():          # Auswahl Einzelspiel gegen den Computer oder Zweispielermodus 
    print("To quit the game or start a new one press q.")
    p = input("How many players?\nOne player (1) or two players (2)? ")
    if p == "1":
        game.players = "1"  # Speichert die Eingabe in dem Attribut game.players
    elif p == "2":
        game.players = "2"
    elif p == "q" or "Q":   # q um das Spiel abzubrechen
        new_game()        
    else:                   # Falsche Eingabe
        print("No way, dude!")
        players()
    make_board()

def make_board():           # Groesse des Spielfelds wird festgelegt
    board.matrix = dict()
    print("Ok, and now the size of the board:")
    r = input("How many rows? ")
    c = input("How many columns? ")
    if int(r) < 4 or int(c) < 4:
        print("No way, dude!")
        make_board()
    else:
        game.rows = r       # Das Attribut game.rows speichert die eingegebene Anzahl der Reihen 
        game.columns = c    # Das Attribut game.columns speichert die eingegebene Anzahl der Spalten
    blank_board()

def blank_board():          # Erstellt ein Spielfeld mit leeren Zellen und speichert es in board.matrix
    board.full = 0          # Setzt board.full bei jedem neuen Spiel auf null
    board.blank = "|___"
    board.matrix = dict()   # Dictionary welches für jede Zelle einen Wert speichert
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            board.matrix[(x, y)] = board.blank  # Alle Zellen leer
    print_board()
    game()

def print_board():
    board.one = "|_X_"      # Symbol für eine von Spieler 1 belegte Zelle
    board.two = "|_O_"      # Symbol für eine von Spieler 2 belegte Zelle
    table = ""
    print ("\n###### VIER GEWINNT ######\n")
    for x in range(int(game.rows)):                 # Für jede Zeile
        for y in range(int(game.columns)):          # Für jede Spalte
            if board.matrix[(x, y)] == board.blank: # Check ob Zelle leer
                table += board.blank                # druckt leere Zelle
            elif board.matrix[(x, y)] == board.one: # Check ob Zelle von Spieler 1 belegt
                table += board.one                  # druckt Zelle mit Chip von Spieler 1
            elif board.matrix[(x, y)] == board.two: # Check ob Zelle von Spieler 2 belegt
                table += board.two                  # druckt Zelle mit Chip von Spieler 2
        table += "|\n"
    for x in range(int(game.columns)):  # Bezeichnung der Spalten
        table += "  " + str(x+1) + " "
    table += "\n"
    board.full += 1     # Bei jedem Zug wird board.full um 1 erhoeht, bis die maximale Anzahl an Zügen erreicht ist
    print(table)        # Druckt die Werte aller Zellen als Spielfeld nach jedem Spielzug

def pvp():      # Spielablauf Zweispielermodus
    player_1()
    player_2()
    pvp()

def pvcpu():    # Spielablauf Einzelspielermodus
    player_1()
    player_cpu()
    pvcpu()

def player_1(): # Spieler 1 ist am Zug
    board.insert = input("Put a disc, Player 1 >>> ")   # Attribut board.insert speichert Eingabe des Spielers, in welche Spalte der Chip geworfen werden soll
    try:        # falls Spalte noch nicht voll, dann versuchen auszuführen
        if board.insert.isdigit() == True:  # Wenn board.insert eine Zahl ist
            board.insert = int(board.insert)
            if board.insert in range(int(game.columns)+1):
                i = int(game.rows)-1
                if board.matrix[(i, (int(board.insert)-1))] == board.blank: # Wenn Zelle leer, dann setze Chip in unterste Zelle der gewählten Spalte
                    board.matrix[(i, (int(board.insert)-1))] = board.one
                else:
                    while board.matrix[(i, (int(board.insert)-1))] != board.blank: # Wenn Zelle belegt, dann teste Zelle darueber
                        i -= 1
                    board.matrix[(i, (int(board.insert)-1))] = board.one
                print_board()   # Drucke aktualisiertes Board
                win_check()     # Gewinncheck
            else:
                print("No way, dude!")  # Falsche Eingabe
                player_1()
        else:
            print("No way, dude")
            player_1()
    except KeyError:    # Bei voll besetzter Spalte
        player_1()


def player_2(): # Spieler 2 ist am Zug
    board.insert = input("Put a disc, Player 2 >>> ")
    try:
        if board.insert.isdigit() == True:
            board.insert = int(board.insert)
            if board.insert in range(int(game.columns)+1):
                i = int(game.rows)-1
                if board.matrix[(i, (int(board.insert)-1))] == board.blank:
                    board.matrix[(i, (int(board.insert)-1))] = board.two
                else:
                    while board.matrix[(i, (int(board.insert)-1))] != board.blank:
                        i -= 1
                    board.matrix[(i, (int(board.insert)-1))] = board.two
                print_board()
                win_check()
            else:
                print("No way, dude!")
                player_2()
        else:
            print("No way, dude!")
            player_2()
    except KeyError:
        player_2()

def player_cpu():   # Computer ist am Zug
    board.insert = random.randint(0, int(game.columns)) # Wählt zufällig eine Spalte aus
    try:     
        if board.insert in range(int(game.columns)+1):
                i = int(game.rows)-1
                if board.matrix[(i, (int(board.insert)-1))] == board.blank:
                    board.matrix[(i, (int(board.insert)-1))] = board.two
                else:
                    while board.matrix[(i, (int(board.insert)-1))] != board.blank:
                        i -= 1
                    board.matrix[(i, (int(board.insert)-1))] = board.two
                print_board()
                win_check()
        else:
            player_cpu()
    except KeyError:
        player_cpu()

def new_game(): # Beendet das Spiel oder startet ein neues
    new = input("Do you want start a new game (n) or quit (q)? ")
    if new == "n" or new == "N":    # Startet neues Spiel
        connectfour()
    elif new == "q" or new == "Q":  # Beendet das Spiel
        quit()
    else:
        print("No way, dude!")      # Falsche Eingabe
        new_game()

def game(): # Startet entweder Einzelspielermodus und Zweispielermodus
    if game.players == "1": # Einzelspielermodus
        pvcpu()
    elif game.players == "2":   # Zweispielermodus
        pvp()

def full_check():   # Check ob das Spielfeld voll ist
    cells = int(game.rows) * int(game.columns) + 1  # Maximale Anzahl an Zügen auf dem Spielfeld
    if board.full == cells: # Wenn das Attribut board.full die Anzahl der maximalen Züge erreicht hat
        print("\n##################################\n###### Nobody wins the game ######\n##################################\n")
        new_game()  # Wenn Spielfeld voll, dann neues Spiel oder Spiel verlassen
    else:           # Wenn das Spielfeld noch nicht voll, dann weiter verfahren
        pass

def win_check():    # Gewinncheck
    full_check()
    win_vertical()  # vertikaler Check
    win_horizontal()    # horizontaler Check
    win_diagonal_down() # diagonal absteigend
    win_diagonal_up()   # diagonal aufsteigend

def win_vertical(): # Vertikal vier gleiche Zellen
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:    # Wenn diese Bedingungen erfuellt sind, gewinnt Spieler 1 oder Spieler 2
                if board.matrix[(x, y)] == board.one and board.matrix[(x+1, y)] == board.one and board.matrix[(x+2, y)] == board.one and board.matrix[(x+3, y)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x+1, y)] == board.two and board.matrix[(x+2, y)] == board.two and board.matrix[(x+3, y)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()
            except KeyError:
                pass

def win_horizontal():   # Horizontal vier gleiche Zellen
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x, y+1)] == board.one and board.matrix[(x, y+2)] == board.one and board.matrix[(x, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x, y+1)] == board.two and board.matrix[(x, y+2)] == board.two and board.matrix[(x, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()
            except KeyError:
                pass

def win_diagonal_down():    # Diagonal absteigend vier gleiche Zellen
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x+1, y+1)] == board.one and board.matrix[(x+2, y+2)] == board.one and board.matrix[(x+3, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x+1, y+1)] == board.two and board.matrix[(x+2, y+2)] == board.two and board.matrix[(x+3, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()       
            except KeyError:
                pass

def win_diagonal_up():      # Diagonal aufsteigend vier gleiche Zellen
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x-1, y+1)] == board.one and board.matrix[(x-2, y+2)] == board.one and board.matrix[(x-3, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x-1, y+1)] == board.two and board.matrix[(x-2, y+2)] == board.two and board.matrix[(x-3, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()                
            except KeyError:
                pass

def connectfour(): # Fuehrt Spiel aus
    players()

connectfour()
