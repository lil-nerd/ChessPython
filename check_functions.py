from desk import *

def check_figure(desk, number):
    
    if desk.chess_field[number].get_symbol() == ' ':
        print("Go")
        print("Choose a figure not a free cell")
        return False
    else:
        return True

def check_step(desk, now, future):
    if now == future:
        return False
    else:
        return True
