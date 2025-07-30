from tkinter import *
from tkinter import messagebox

# Initialize main window
Base = Tk()
Base.geometry("900x600")
Base.title("XO Game")
Base.configure(bg="#1e1e1e")

# Fonts
btn_font = ("Poppins", 16, "bold")
label_font = ("Poppins", 13, "bold")
reset_font = ("Poppins", 13, "bold")

# Game variables
board = [""] * 9
turn = "X"
scores = {"Player-1": 0, "Player-2": 0, "No Result": 0}

# Update score display
def update_scores():
    btn12.config(text=f"{scores['Player-1']}")
    btn13.config(text=f"{scores['Player-2']}")
    btn14.config(text=f"{scores['No Result']}")

# Check win or tie
def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return None

# Handle click
def on_click(index):
    global turn
    if board[index] == "":
        board[index] = turn
        buttons[index].config(text=turn)

        result = check_winner()
        if result:
            if result == "X":
                scores["Player-1"] += 1
                update_scores()
                messagebox.showinfo("Game Over", "Player X wins!")
                return
            elif result == "O":
                scores["Player-2"] += 1
                update_scores()
                messagebox.showinfo("Game Over", "Player O wins!")
                return
            elif result == "Tie":
                scores["No Result"] += 1
                update_scores()
                messagebox.showinfo("Game Over", "It's a tie!")
                return

        turn = "O" if turn == "X" else "X"

# Reset round
def reset_round():
    global board, turn
    board = [""] * 9
    turn = "X"
    for button in buttons:
        button.config(text="")

# Reset entire game
def reset_game():
    global board, turn, scores
    board = [""] * 9
    turn = "X"
    scores = {"Player-1": 0, "Player-2": 0, "No Result": 0}
    update_scores()
    for button in buttons:
        button.config(text="")

# Hover effect
def on_enter(e):
    e.widget['background'] = '#e6e6e6'
def on_leave(e):
    e.widget['background'] = '#f0f0f0'

# Create 3x3 buttons
buttons = []
for i in range(9):
    btn = Button(Base, bg="#f0f0f0", fg="#222", width=10, height=4,
                 font=btn_font, relief="groove", bd=3,
                 activebackground="#d1d1d1", activeforeground="#000",
                 command=lambda i=i: on_click(i))
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    buttons.append(btn)

# Grid positions
grid_start_x = 180
grid_start_y = 80
gap = 100

for row in range(3):
    for col in range(3):
        idx = row * 3 + col
        buttons[idx].place(x=grid_start_x + col * gap, y=grid_start_y + row * gap)

# Score Labels
Label(Base, text="Player 1 (X)", font=label_font, bg="#1e1e1e", fg="#00ffcc").place(x=600, y=100)
Label(Base, text="Player 2 (O)", font=label_font, bg="#1e1e1e", fg="#00ffcc").place(x=600, y=210)
Label(Base, text="No Result", font=label_font, bg="#1e1e1e", fg="#00ffcc").place(x=600, y=320)

# Score Buttons
btn12 = Button(Base, width=10, height=2, text="0", bg="#2c2c2c", fg="#ffffff",
               font=btn_font, relief="flat")
btn13 = Button(Base, width=10, height=2, text="0", bg="#2c2c2c", fg="#ffffff",
               font=btn_font, relief="flat")
btn14 = Button(Base, width=10, height=2, text="0", bg="#2c2c2c", fg="#ffffff",
               font=btn_font, relief="flat")

btn12.place(x=600, y=140)
btn13.place(x=600, y=250)
btn14.place(x=600, y=360)

# Reset buttons
btn10 = Button(Base, bg="#ff6666", fg="#fff", text="Reset Game", width=14, height=2,
               font=reset_font, relief="raised", bd=2, activebackground="#ff4d4d",
               command=reset_game)
btn10.place(x=180, y=430)

btn11 = Button(Base, bg="#66b3ff", fg="#fff", text="Reset Round", width=14, height=2,
               font=reset_font, relief="raised", bd=2, activebackground="#3399ff",
               command=reset_round)
btn11.place(x=380, y=430)

# Start
Base.mainloop()
