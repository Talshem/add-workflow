import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = ['' for _ in range(9)]
        self.current_player = 'X'

        self.buttons = [tk.Button(root, text='', font=('normal', 40), width=5, height=2, 
                                  command=lambda i=i: self.on_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

    def on_click(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                          (0, 4, 8), (2, 4, 6)]

        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != '':
                return True
        return False

    def reset_board(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
