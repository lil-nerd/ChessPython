
figure_names = ['Free', 'Pawn', 'Knight', 'Rook', 'Bishop', 'Queen', 'King']
figure_symbols_white = [' ',  u'\u2659', u'\u2658', u'\u2657', u'\u2656', u'\u2655', u'\u2654']
figure_symbols_black = [u'\u265F', u'\u265E', u'\u265D', u'\u265C', u'\u265B', u'\u265A']
figure_types = [0, 1, 2, 3, 4, 5, 6]

class Figure:
    
    def __init__(self):
        self.f_type = figure_types[0]
        self.f_addr = -1
        self.f_color = 0
        
    def create_figure(self, ftype, bw):
        self.f_type = ftype
        self.f_color = bw
    
    def place_figure(self, address):
        self.f_addr = address
    
    def get_symbol(self):
        if self.f_color == -1:
            return figure_symbols_black[self.f_type - 1]        
        else:
            return figure_symbols_white[self.f_type]
        
    
