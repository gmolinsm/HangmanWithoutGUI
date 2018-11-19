import random
from tkinter import *
from PIL import Image, ImageTk


class UI:
    def __init__(self, window):

        # Game logic
        self.random = random.randint(0, 9)
        self.temp_solution = ""
        self.solution = list()
        self.progress = list()
        self.view_progress = list()

        self.index = 0
        self.words = []
        fd = open("Words", "r")
        for line in fd:
            if self.index == self.random:
                self.temp_solution = line
            self.index += 1

        for i in range(len(self.temp_solution) - 1):
            if self.temp_solution[i] == " ":
                self.view_progress.append(" ")
            else:
                self.view_progress.append("_")
                self.progress.append("")
                self.solution.append(self.temp_solution[i])

        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.stages = ["assets/S1.png", "assets/S2.png", "assets/S3.png", "assets/S4.png",
                  "assets/S5.png", "assets/S6.png", "assets/S8.png", "assets/S10.png"]
        self.lives = 8
        self.wrong_letters = ""

        self.window = window
        self.idx = 0
        window.title("Hangman")
        self.title_font = ("Times New Roman", 40)
        self.solution_font = ("Times New Roman", 20)
        self.alphabet_font = ("Times New Roman", 10)
        self.buttons_font = ("Times New Roman", 20)

        # Hangman viewport
        self.stage_list = []
        self.count = 0
        for i in range(8):
            self.stage_list.append(ImageTk.PhotoImage(Image.open(self.stages[i])))
        self.viewport = Label(master=window, image=self.stage_list[self.count])
        self.viewport.image = self.stage_list[self.count]
        self.viewport.grid(row=2, column=0)

        # Text
        self.lbl1 = Label(master=window, text="Hangman", font=self.title_font)
        self.lbl1.grid(row=0, column=1)

        self.lbl2 = Label(master=window, text=str(self.view_progress), font=self.solution_font)
        self.lbl2.grid(row=3, column=1)

        self.lbl3 = Label(master=window, text=str(self.wrong_letters) + " " + str(self.lives-1), font=self.solution_font)
        self.lbl3.grid(row=2, column=1)

        # Buttons
        self.buttons = []
        self.gridpos = []
        column = 2
        for i in range(0, len(self.alphabet)):
            self.buttons.append(Button(master=window, text=self.alphabet[i], width=2,
                                       font=self.alphabet_font, command=self.check)) # ????????????????????????
            self.gridpos.append(self.buttons[i].grid(row=1, column=column))
            column += 1

        close = Button(master=window, text="Exit", width=6, font=self.buttons_font, command=self.close)
        close.grid(row=1, column=0)

    def close(self):
        exit(0)

    # This will refresh data on screen
    def update_view(self):
        self.lbl2["text"] = str(self.view_progress)
        self.lbl3["text"] = str(self.wrong_letters) + str(self.lives - 1)
        self.viewport["image"] = self.stage_list[self.count]

    def check(self):
        letter = "a"
        correct = False
        index = 0
        index_with_space = 0
        for character in self.solution:
            if self.temp_solution[index_with_space] == " ":
                index_with_space += 1
            if character == letter:
                self.view_progress[index_with_space] = letter
                self.progress[index] = letter
                correct = True
            index_with_space += 1
            index += 1
        if correct:
            print()
            print(self.view_progress)
            print()
            if self.progress == self.solution:
                self.close()
                print("Congratulations, you WON!")
        else:
            self.lives -= 1
            self.count += 1
            if self.lives == 0:
                print()
                print("Tough luck, you reached the maximum failed attempts... GAME OVER")
                print()
                print("The self.solution was:", self.solution)
                window.after(50000, self.close())
            else:
                self.wrong_letters += letter + " "
                print()
                print("Incorrect! You have", self.lives-1, "failed attempts left...")
                print("Wrong letters:", self.wrong_letters)
                print()
                print(str(self.view_progress))
                print()
        self.update_view()


window = Tk()
self = UI(window)
window.mainloop()