from tkinter import *
from PIL import Image, ImageTk
import random

def computerSide():
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    elif computer == 3:
        computer = "scissors"
    else:
        computer = "error"
    return computer

def play():
    computer = computerSide()
    if player.get() == computer:
        result.set("tie, you both selected the same")
    elif player.get() == "rock" and computer == "paper":
        result.set("you lose, paper beats rock")
    elif player.get() == "rock" and computer == "scissors":
        result.set("you win, rock beats scissors")
    elif player.get() == "paper" and computer == "scissors":
        result.set("you lose, scissors beats paper")
    elif player.get() == "paper" and computer == "rock":
        result.set("you win, paper beats rock")
    elif player.get() == "scissors" and computer == "rock":
        result.set("you lose, rock beats scissors")
    elif player.get() == "scissors" and computer =="paper":
        result.set("you win, scissors beats paper")
    else:
        result.set("invalid, something went wrong")

def reset():
    result.set("")
    player.set("")

def exit():
    window.destroy()

def select(option):
    return player.set(option)

window = Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Rock Paper Scissors")
window.config(bg="seashell3")

player = StringVar()
result = StringVar()
Label(window, text="choose any one: ", font="arial 15 bold", bg="seashell2").place(x=20, y=70)
Button(window, font="arial 13 bold", text="rock", padx=5, bg="seashell4", command=lambda: select('rock')).place(x=30, y=130)
Button(window, font="arial 13 bold", text="paper", padx=5, bg="seashell4", command=lambda: select('paper')).place(x=160, y=130)
Button(window, font="arial 13 bold", text="scissors", padx=5, bg="seashell4", command=lambda: select('scissors')).place(x=300, y=130)

Entry(window, font="arial 10 bold", textvariable=result, bg="antiquewhite2", width=50).place(x=25, y=250)
Button(window, font="arial 13 bold", text="PLAY", padx=5, bg="seashell4", command=play).place(x=150, y=190)
Button(window, font="arial 13 bold", text="RESET", padx=5, bg="seashell4", command=reset).place(x=70, y=310)
Button(window, font="arial 13 bold", text="EXIT", padx=5, bg="seashell4", command=exit).place(x=230, y=310)
window.mainloop()