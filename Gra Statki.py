#Gra w statki

from random import choice

##Pobiera wymiary planszy
def take_parametrs():
    a = True
    while a:
        try:
            width = int(input("Podaj szerkokość planszy "))
            a = False
        except:
            print("Podaj liczbę całkowitą")

    b = True
    while b:
        try:
            length = int(input("Podaj długość planszy "))
            b = False
        except:
            print("Podaj liczbę całkowitą")

    return width, length

##Tworzy plansze od pobranych parametrów
def make_board(args_from_take_parametrs):

    width = args_from_take_parametrs[0]
    length = args_from_take_parametrs[1]


    board = []

    for x in range(width):
        board.append(['~'] * length)

    return board

##Rysuje plansze utworzoną w funkcji make_board i zapisuje ją do pliku po każdej turze gracza /useless/
def print_board(board_from_make_board):

    for row in board_from_make_board:
        print(" ".join(row))

    board_file = open('Plansza.txt', 'w')
    board_file.write(str(board))
    board_file.close()

##Losuje ilość statków którą podaje gracz ze wszytskich pól na planszy
def make_ship(board_parametrs,ask_ships):
    ships = []
    board_fields = []
    for x in range(board_parametrs[0]):
        for y in range(board_parametrs[1]):
            field = [x,y]
            board_fields.append(field)

    for z in range(ask_ships):
        ship = choice(board_fields)
        print('\n',ship,'statek') #DEBUG
        ships.append(ship)
        print('\n',ships,'dodaje')#DEBUG
        board_fields.remove(ship)
        print('\n',board_fields,'usuwam')#DEBUG

    return ships

##Pobiera wiersze i kolumny ktore podaje gracz aby odgadnac statek
def ask_player():
    a = True
    while a:
        try:
            ask_row = int(input("\nZagadnij wiersz ")) - 1
            a = False
        except:
            print("Zła wartość pola, Spróbuj ponownie")

    b = True
    while b:
        try:
            ask_col = int(input("Zagadnij kolumnę ")) - 1
            b = False
        except:
            print("Zła wartość pola, Spróbuj ponownie")

    asking = [ask_row, ask_col]
    return asking

def ask_ships(board_parameters):
    a = True
    while a:
        try:
            ships = int(input("\nIle statków wybierasz "))
            a = False
        except:
            print("Podaj całkowitą liczbę statków")

    while ships > board_parameters[0] * board_parameters [1]:
        print('\nUtwórz mniej statków')
        ships = int(input("\nIle statków wybierasz "))
    return ships

def alive_ships(ships):
    list_alive_ships = []
    for x in ships:
        a = x[0]
        b = x[1]
        alive_ship = [a+1, b+1]
        list_alive_ships.append(alive_ship)

    return list_alive_ships

def game(ships):

    a = True
    while a:
        try:
            turn = int(input("Ile rund wybierzasz "))
            a = False
        except:
            print("Podaj całkowitą liczbę tur")

    while turn < len(ships):
        print("Za mało")
        turn = int(input("Ile rund wybierzasz "))

    rond = 1

    while len(ships) > 0:
        if turn < rond:
            print_board(board)
            al_ships = alive_ships(ships)
            print('Przegrałeś pozostało ', len(ships),' statków, na polach', al_ships)
            break
        else:
            print("#########RUNDA", str(rond), "#########")
            print_board(board)
            b = True
            rond = rond + 1
            while b:
                try:
                    shoot = ask_player()


                    if shoot in ships:
                        board[shoot[0]][shoot[1]] = 'F'
                        ships.remove(shoot)
                        print("\nTrafiłeś\nPozostało",len(ships),"statków")


                    elif board[shoot[0]][shoot[1]] == 'O':
                        print("\nTu już strzelałeś")
                        rond = rond - 1

                    else:
                        print("\nPudło")
                        board[shoot[0]][shoot[1]] = 'O'

                    b = False
                except:
                    print("Poza mapą, podaj poprawne współrzędne")


    if len(ships) == 0:
        print("\nWygrałeś")

    for live_ship in ships:
        board[live_ship[0]][live_ship[1]] = 'P'

    print_board(board)

board_args = take_parametrs()
board = make_board(board_args)
print_board(board)
ship = make_ship(board_args,ask_ships(board_args))
game(ship)