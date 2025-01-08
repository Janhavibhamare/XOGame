from tkinter import *

# Initialize the main window
Base = Tk()
Base.geometry("600x300")
Base.title("XO Game")

# Fonts
f1 = ("Arial Bold", 8)

# Game variables
board = [""] * 9
turn = "X"
scores = {"Player-1": 0, "Player-2": 0, "No Result": 0}

# Update Score Display
def update_scores():
    btn12.config(text=f"{scores['Player-1']}")
    btn13.config(text=f"{scores['Player-2']}")
    btn14.config(text=f"{scores['No Result']}")

# Check for a winner or tie
def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8)   # Columns
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]  # Return the winner
    if "" not in board:
        return "Tie"  # Return tie if all cells are filled
    return None  # No winner yet

# Button click handler
def on_click(index):
    global turn

    if board[index] == "":  # Ensure the cell is empty
        board[index] = turn
        buttons[index].config(text=turn)

        result = check_winner()
        if result:
            if result == "X":
                scores["Player-1"] += 1
                update_scores()
                return
            elif result == "O":
                scores["Player-2"] += 1
                update_scores()
                return
            elif result == "Tie":
                scores["No Result"] += 1
                update_scores()
                return

        # Switch turn
        turn = "O" if turn == "X" else "X"

# Reset Round Functionality
def reset_round():
    global board, turn
    board = [""] * 9  # Reset the board
    turn = "X"  # Reset the turn to Player 1
    for button in buttons:
        button.config(text="")  # Clear button labels

# Reset Game Functionality
def reset_game():
    global board, turn, scores
    board = [""] * 9  # Reset the board
    turn = "X"  # Reset the turn to Player 1
    scores = {"Player-1": 0, "Player-2": 0, "No Result": 0}  # Reset scores
    update_scores()  # Update score display
    for button in buttons:
        button.config(text="")  # Clear button labels

# Buttons for the 3x3 grid
buttons = [Button(Base, bg="White",width=10, height=2, command=lambda i=i: on_click(i)) for i in range(9)]

# Place the grid buttons
buttons[0].place(x=20, y=20)
buttons[1].place(x=100, y=20)
buttons[2].place(x=180, y=20)
buttons[3].place(x=20, y=60)
buttons[4].place(x=100, y=60)
buttons[5].place(x=180, y=60)
buttons[6].place(x=20, y=100)
buttons[7].place(x=100, y=100)
buttons[8].place(x=180, y=100)

# Reset buttons
btn10 = Button(Base, bg="white", text="Reset Game", width=15, height=3, font=f1, command=reset_game)
btn10.place(x=20, y=150)

btn11 = Button(Base, bg="white", text="Reset Round", width=15, height=3, font=f1, command=reset_round)
btn11.place(x=150, y=150)

# Score Display Buttons
btn12 = Button(Base, width=15, height=2, text="0", bg="white")
btn13 = Button(Base, width=15, height=2, text="0", bg="white")
btn14 = Button(Base, width=15, height=2, text="0", bg="white")

btn12.place(x=460, y=20)
btn13.place(x=460, y=60)
btn14.place(x=460, y=100)

# Labels for the scores
lb1 = Label(Base, font=f1, text="Player-1")
lb1.place(x=400, y=30)

lb2 = Label(Base, font=f1, text="Player-2")
lb2.place(x=400, y=70)

lb3 = Label(Base, font=f1, text="No Result")
lb3.place(x=400, y=110)

# Start the GUI
Base.mainloop()
