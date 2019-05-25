#!/usr/bin/python
from __future__ import print_function
from class_figures import Figure
from window import SquareButton
from tkinter import *
from functools import *
from check_functions import *

class Desk:

    btn_array = []
    selected_figure = -1  
    current_player = 1
    step_status = True
    
    def __init__(self):
        self.chess_field = []
    
    
    def new_desk(self):
        
        array = [4, 2, 3, 5, 6, 3, 2, 4, 
                 1, 1, 1, 1, 1, 1, 1, 1, 
                 0, 0, 0, 0, 0, 0, 0, 0, 
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 4, 2, 3, 5, 6, 3, 2, 4]
        
        for i in range(64):
            
            fig = Figure()
            if i < 16:
                fig.create_figure(array[i], -1)
            if i >= 16 and i < 48:
                fig.create_figure(array[i], 0)
            if i >= 48:
                fig.create_figure(array[i], 1)
            fig.place_figure(i)
            
            self.chess_field.append(fig)
        
        print("Desk is ready")
        
        
        
    def make_move(self, number):
        
        if Desk.step_status:
            
            if check_figure(self, number, Desk.current_player):
                
                Desk.step_status = not Desk.step_status
                Desk.selected_figure = number
                Desk.btn_array[number].config(background= "green")
                
                
        else:
            
            if check_step(self, Desk.selected_figure, number, Desk.current_player):
                
                self.chess_field[number] = self.chess_field[Desk.selected_figure]
                Desk.btn_array[number].config(text= self.chess_field[number].get_symbol())
            
            
                figure = Figure()
                figure.place_figure(Desk.selected_figure)
                self.chess_field[Desk.selected_figure] = figure
                
                cell_colors = ["white", "grey"]
                Desk.btn_array[Desk.selected_figure].config(text= self.chess_field[Desk.selected_figure].get_symbol(), background= cell_colors[(Desk.selected_figure // 8 + Desk.selected_figure % 8 ) % 2])
            
                Desk.step_status = not Desk.step_status
                Desk.current_player = Desk.current_player * (-1)
                print(Desk.selected_figure)
            
        
        
    def show_desk(self):
    
        field_rows = field_cols = 8
    
        root = Tk()
        root.title("Chess")
        root.geometry("1000x1000")
 
        cell_colors = ["white", "grey"]
        b = 0 

        for f_row in range(field_rows):
            for f_col in range(field_cols):
                cell_text = self.chess_field[f_row * 8 + f_col].get_symbol()
                btn = SquareButton(root, side_length= 80, background= cell_colors[b], activebackground= "green", text = cell_text, font= 'arial 60', relief= FLAT, command= partial(self.make_move, f_row * 8 + f_col))
                btn.grid(row= f_row, column= f_col)
                
                Desk.btn_array.append(btn)
                
                b = not b
            b = not b

        
 
        root.mainloop()
    
   
    def print_desk(self):

        for i in range(64):
            print(self.chess_field[i].get_symbol(), end=' ')
            if i % 8 == 7:
                print()
		
        
            
        
