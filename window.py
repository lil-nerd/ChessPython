from tkinter import *




class SquareButton(Button):
    def __init__(self, master=None, **kwargs):
        self.img = PhotoImage()
        n = kwargs.pop('n', None)
        side = kwargs.pop('side_length', None)
        Button.__init__(self, master, image=self.img, compound='center', **kwargs)
        if side:
            self.config(width=side, height=side)
        
    
