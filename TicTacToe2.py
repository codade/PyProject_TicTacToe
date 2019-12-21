
board=[' ']*10
avail=[str(num) for num in range(0,10)]
def display_board(a,b):
    print('   Spiel-\t   Mögliche\n'+
          '   stand\t  Spielzüge\n\n '+
         ' '+a[7]+' | '+a[8]+' | '+a[9]+' \t  '+b[7]+' | '+b[8]+' | '+b[9]+' \n '+
         '---+---+---'+'\t '+'---+---+---\n '+
         ' '+a[4]+' | '+a[5]+' | '+a[6]+' \t  '+b[4]+' | '+b[5]+' | '+b[6]+' \n '+
          '---+---+---'+'\t '+'---+---+---\n '+
         ' '+a[1]+' | '+a[2]+' | '+a[3]+' \t  '+b[1]+' | '+b[2]+' | '+b[3]+' \n')    
display_board(board, avail)

def namens():
    player1=input('Ich bin neugierig, wie heißen Sie?: ').capitalize()
    player2=input('Und wie heißt Ihr Mitspieler?').capitalize()
    return [0,player1,player2]

def player_input(names,dran):
    marker=''
    while not (marker=='X' or marker=='O'):
        if durchgang==0:
            marker=input(f'{names[dran]} wählen Sie jetzt, ob Sie X oder O spielen möchten! ').upper()
        else:
            marker=input(f'{names[dran]} mit welchem Symbol wollen Sie dieses Mal ins Rennen steigen: X oder O?').upper()
        if not (marker=='X' or marker=='O'):
            print('Sie können nur X oder O eingeben!')
            continue
    if (marker=='X' and dran==1) or (marker=='O' and dran==-1) :
        return [0,'X','O']
    else:
        return [0,'O','X']

def place_marker(board, avail, marker, position):
    board[position]=marker
    avail[position]=' '

def win_check(board, mark):
    return ((board[7] ==  board[8] ==  board[9] == mark) or # across the top
    (board[4] ==  board[5] ==  board[6] == mark) or # across the middle
    (board[1] ==  board[2] ==  board[3] == mark) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == mark) or # down the middle
    (board[8] ==  board[5] ==  board[2] == mark) or # down the middle
    (board[9] ==  board[6] ==  board[3] == mark) or # down the right side
    (board[7] ==  board[5] ==  board[3] == mark) or # diagonal
    (board[9] ==  board[5] ==  board[1] == mark)) # diagonal
def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(names, dran, board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
	    position=int(input(f'{names[dran]}, bitte wählen Sie ein Feld für Ihren nächsten Zug: '))
        except:
	    print('Sie können nur eine Zahl eingeben!)
	else:
	    if position not in [1,2,3,4,5,6,7,8,9]:
        	print(f'{names[dran]} bitte wählen Sie einen Wert zwischen 1 und 9.')
            elif not space_check(board, position):
               print(f'{names[dran]}, dieses Feld ist leider schon besetzt! Wählen Sie ein anderes!')
    return position 

def replay(names,dran):
    again=''
    while not (again=='j' or again=='n'):
        if win_check(board,playmark): 
            again=input(f'{names[dran]}, trauen Sie sich trotz Gewinn noch eine Revanche zu? Ja oder Nein:')[0].lower()
        elif win_check(board,playmark): 
            again=input(f'{names[dran]}, trauen Sie sich trotz Gewinn noch eine Revanche zu? Ja oder Nein:')[0].lower()
        else:
            again=input('Wollen Sie diesen Patt so stehen lassen oder noch einmal alles geben? Ja oder Nein:')[0].lower()
        if not (again=='j' or again=='n'):
            print('Sie können nur ja oder nein eingeben!')
    return again=='j'
    pass

def start():
    start=0
    starter=True
    while not (start=='j' or start=='n'):
        start = input('Möchten Sie das Spiel starten und weitere Informationen bekommen? Ja oder Nein: ')[0].lower()
        if not (start=='j' or start=='n'):
            print('Sie können nur ja oder nein eingeben.')
        elif start=='n':
            print('\nSchönen Tag noch und bis bald mal wieder!')
            return starter==False   
    return starter


##Zusammengesetzte Spielfunktion
from IPython.display import clear_output
import random
print('Willkommen zu Tic Tac Toe!')
starter=start()
durchgang=0
board=[' ']*10
avail=[str(num) for num in range(0,10)]
while starter==True: 
    print('\n'*100)
    board=[' ']*10
    avail=[str(num) for num in range(0,10)]
    dran=random.choice((-1,1))
    running=True
    if durchgang==0:
        print('Sie sehen links einen aktuellen Spielstand und rechts die möglichen Felder nummeriert von 1-9:\n')
        display_board(board,avail)
        print('\nZiel des Spiels ist es drei Felder in einer Reihe (senkrecht, waagrecht oder diagonal) mit dem Symbol "X" oder "O" zu füllen.')
        names=namens()
        print('\n'*100)
        print(f'Der Zufall hat entschieden, dass {names[dran]} starten darf')
        playmarker=player_input(names,dran)
        print(f'\nNa dann los! {names[dran]} spielt mit {playmarker[dran]}.\n\n')   
    else: 
        print('Die Spielregeln können Sie ja jetzt schon im Schlaf.\n')
        print(f'Der Zufall hat entschieden: Es startet {names[dran]}')
        playmarker=player_input(names, dran)
        print(f"\nNa dann auf in eine neue Runde, {names[dran]}! {playmarker[dran]} bringt Ihnen bestimmt Glück\n\n")
    while running:
        playmark=playmarker[dran]
        display_board(board,avail)
        position=player_choice(names, dran, board)
        place_marker(board, avail, playmark, position)
        
        if win_check(board, playmark):
            display_board(board,avail)
            print(f'Herzlichen Glückwunsch {names[dran]}! Sie haben gewonnen!')
            running=False
        else:
            if full_board_check(board):
                display_board(board,avail)
                print('Welch spannendes Spiel und dennoch ein knapper Ausgang mit Patt.\nKeiner gewinnt!\n')
                running=False
            else:
                dran *=-1
                print('\n'*100)
        
    if replay(names,dran):
        durchgang+=1
        continue
    else:
        starter=False
        print('\n\nHoffentlich hat es Spaß gemacht!')
	

