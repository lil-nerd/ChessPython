from desk import *

legal_pawn_X = [0, 0]
legal_pawn_Y = [1, 2]
legal_pawn = [legal_pawn_X, legal_pawn_Y]

legal_steps = [legal_pawn]



def get_pair(number):
    return [number % 8, number // 8]
def get_number(x, y):
    return y * 8 + x

def check_figure(desk, number, current_player):
    
    if current_player != desk.chess_field[number].f_color:
        print("Choose your figure")
        return False
    else:
        return True

def check_step(desk, now, future, current_player):
    
    if current_player == desk.chess_field[future].f_color:
        print("Go")
        return False
    
    else:
        legal = create_step_dictionary(desk, now, current_player)
        if desk.chess_field[now].f_type == 1:
            if future in legal:
                return True
            else:
                return False
            
        return True


def create_step_dictionary(desk, now, current_player):
    
    steps = []
    pair = get_pair(now)
    
    #PAWN_LEGAL_MOVES
    if desk.chess_field[now].f_type == 1:
        for i in range(len(legal_steps[desk.chess_field[now].f_type - 1])):
            
            step = get_number((-1) * current_player * legal_steps[desk.chess_field[now].f_type - 1][0][i] + pair[0], 
                              (-1) * current_player * legal_steps[desk.chess_field[now].f_type - 1][1][i] + pair[1])
            steps.append(step)
            
        
        if current_player == 1 and pair[1] != 6:
            steps.pop()
        if current_player == -1 and pair[1] != 1:
            steps.pop()
        
        
        
            
        
    return steps
                                                                        
            
            
        
        
        
        
