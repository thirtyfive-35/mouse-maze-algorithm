import tkinter as tk
from tkinter import messagebox
import os 

class Odev:
    def __init__(self):
        self.fare_labirenti = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
            [0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0],
            [0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0],
            [0,1,1,1,1,1,0,1,1,0,1,0,0,0,1,0],
            [0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0],
            [0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0],
            [0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0],
            [0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        self.dizin = os.getcwd()
        self.mouse_x, self.mouse_y = 5,12
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=640, height=400)
        self.canvas.pack()
        self.root.title("Fare Labirenti")
        self.labirent_olustur()
        self.add_button()
        self.add_peynir()
        self.add_fare()
        
        

        self.root.mainloop()
        
    def add_button(self):
        self.mouse_x, self.mouse_y = 5,12
        button = tk.Button(self.root, text="Move",width=10,height=2,bg="lightgreen", command=self.move_fare)
        button.pack(side="bottom")

    def labirent_olustur(self):
        for row in range(10):
            for col in range(16):
                if self.fare_labirenti[row][col] == 0:
                    self.canvas.create_rectangle(col*40, row*40, (col+1)*40, (row+1)*40, fill="green")
                else:
                    self.canvas.create_rectangle(col*40, row*40, (col+1)*40, (row+1)*40, fill="#BABAB9")
    def add_fare(self):

        self.mouse_x, self.mouse_y = 5,12
        
        self.fare_image = tk.PhotoImage(file=self.dizin + "\\fare.png")
        self.fare = self.canvas.create_image(self.mouse_y*40, self.mouse_x*40, anchor=tk.NW, image=self.fare_image)


    def move_fare(self):

        probable_move = [[self.mouse_x - 1, self.mouse_y], [self.mouse_x + 1, self.mouse_y], [self.mouse_x, self.mouse_y - 1], [self.mouse_x, self.mouse_y + 1]]

        min_val = float('inf')
        min_move = []
        for move in probable_move:

            if 0 <= move[0] <= 9 and 0 <= move[1] <= 15 and self.fare_labirenti[move[0]][move[1]] != 0:
                val = self.fare_labirenti[move[0]][move[1]]
                if val < min_val:
                    min_val = val
                    min_move = move
                    
        if min_move:
            self.canvas.coords(self.fare, min_move[1]*40, min_move[0]*40)
            self.fare_labirenti[min_move[0]][min_move[1]] = self.fare_labirenti[min_move[0]][min_move[1]] + 1
            self.mouse_x, self.mouse_y = min_move[0], min_move[1]
            if self.mouse_x == 8 and self.mouse_y == 12:
                answer = messagebox.showinfo("Oyunu Kazandınız", "Fare peyniri buldu!!")
    def add_peynir(self):
        self.peynir_image = tk.PhotoImage(file= self.dizin +"\peynir.png")
        self.canvas.create_image(12*40, 8*40, anchor=tk.NW, image=self.peynir_image)

dd = Odev()