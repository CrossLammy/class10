import random
weppons = ['Rock','Scissors','Paper']

def show_wp(w):
    text_wp = weppons[w-1]
    return text_wp

def check_win(p1,p2,w1,w2):
    if w1 == w2:
        winner = 'Draw'
    elif w1 == 1 and w2 == 2:
        winner = p1
    elif w1 == 2 and w2 == 3:
        winner = p1
    elif w1 == 3 and w2 == 1:
        winner = p1
    else:
        winner = p2
    return winner

def play_game():
    wp = int(input("'1=Rock','2=Scissors','3=Paper'"))
    wm = random.randint(1,3)
    theWinner = check_win("Playyer","Machine",wp,wm)
    print(f'Playyer --> {show_wp(wp)}')
    print(f'Machine --> {show_wp(wm)}')
    print(f'The Winner is !!! ----> {theWinner}')


def start():
    while True:
        play=input('Play!! (y/n)')
        if play == 'y':
            play_game()
        else:
            print('see you GG')
            break
