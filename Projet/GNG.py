import random
import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter.ttk import *
import math

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("G.N.G")
        self.geometry("959x599")
        self.resizable(False, False)
        self.configure(bg='#7204cc')
        self.iconbitmap("app-mobile-10.ico")
        self.level = tk.StringVar()
        self.level.set("Easy")
        self.create_widgets()
        self.show_home()

    #Créons les différents widgets

    def create_widgets(self):
        self.img0 = tk.PhotoImage(file = f"img0.png")
        self.img1 = tk.PhotoImage(file = f"img1.png")
        self.image = tk.PhotoImage(file=f"background.png")
        self.image2 = tk.PhotoImage(file=f"but.png")
        # Widgets de la page d'accueil
        self.color_label = tk.Label(self, image=self.image)
        self.button_start = tk.Button(self,image=self.image2, font=("Helvetica", 12), command=self.show_game, bg='#2E9AFE', relief=tk.GROOVE)
        self.button_start.pack()
        self.button_start.place(x=0,y=10)
        self.level_select = tk.OptionMenu(self, self.level, "Easy", "Medium", "Hard")
        self.level_select.config(font=("Bradley Hand ITC", 12),bg='white')
        self.level_select.pack()

        # Widgets de la page de jeu
        self.label_answer = tk.Label(self, text="Guess the number", font=("Bradley Hand ITC", 12), bg='#7204cc',fg='white')
        self.entry_answer = tk.Entry(self, font=("Helvetica", 16), relief=tk.GROOVE)
        self.warning= tk.Label(self, font=("Bradley Hand ITC", 12), bg='#7204cc',fg='white',wraplength=300,justify=tk.CENTER)
        self.button_submit = tk.Button(self, text="Submit", font=("Bradley Hand ITC", 12), command=self.check_answer, bg='#9A1AC6', relief=tk.GROOVE,fg='white')
        self.button_restart = tk.Button(self,image=self.img0, font=("Helvetica", 12), command=self.restart_game, bg='white', relief=tk.GROOVE)
        self.button_back = tk.Button(self, image=self.img1, font=("Helvetica", 12), command=self.show_home, bg='white', relief=tk.GROOVE)
        self.label_time = tk.Label(self, text="Remaining Time", font=("Bradley Hand ITC", 12), bg='#7204cc',fg="white")
        self.label_time_remaining = tk.Label(self, font=("Bradley Hand ITC", 12), bg='white')
        self.background_label = tk.Label(self, image=self.image)

        #Création de la fonction qui affiche les widgets de la page d'accueil
        #L'objectif est de pack les widgets de la page d'accueil et de pack_forget() ceux de la page de jeu
    def show_home(self):
        self.running=False
        self.color_label.pack()
        self.color_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.button_start.pack()
        self.button_start.place(x=412,y=545,width=200,height=50)
        self.level_select.pack()
        self.level_select.place(x=0,y=0)
        self.warning.pack_forget()
        self.warning.place(x=0,y=0,width=0,height=0)
        self.label_answer.pack_forget()
        self.label_answer.place(x=0,y=0,width=0,height=0)
        self.entry_answer.pack_forget()
        self.entry_answer.place(x=0, y=0, width=0, height=0)
        self.button_submit.pack_forget()
        self.button_submit.place(x=0,y=0,width=0,height=0)
        self.label_time.pack_forget()
        self.label_time.place(x=0,y=0,width=0,height=0)
        self.label_time_remaining.pack_forget()
        self.label_time_remaining.place(x=0,y=0,width=0,height=0)
        self.button_restart.pack_forget()
        self.button_back.place(x=0, y=0,width=0,height=0)
        self.button_restart.place(x=0, y=0,width=0,height=0)
        self.button_back.pack_forget()
        self.background_label.pack_forget()
        self.background_label.place(x=0, y=0, relwidth=0, relheight=0) 

        #Création de la fonction qui affiche les widgets de la page de jeu
        #L'objectif est de pack les widgets de la page de jeu et de pack_forget() ceux de la page d'accueil
    def show_game(self):
        self.entry_answer.config(state="normal")
        self.button_submit.config(state="normal")
        self.color_label.pack_forget()
        self.color_label.place(x=0, y=0, relwidth=0, relheight=0)
        self.button_start.pack_forget()
        self.button_start.place(x=0,y=0,width=0,height=0)
        self.level_select.pack_forget()
        self.level_select.place(x=0,y=0,width=0,height=0)
        self.background_label.pack()
        self.background_label.place(x=0, y=0, relwidth=0.5, relheight=1) 
        self.label_answer.pack()
        self.label_answer.place(x=640,y=200)
        self.entry_answer.pack()
        self.entry_answer.place(x=569, y=224, width=287, height=56)
        self.button_submit.pack()
        self.button_submit.place(x=648,y=334,width=129,height=42)
        self.label_time.pack()
        self.label_time.place(x=656,y=5)
        self.label_time_remaining.pack()
        self.label_time_remaining.place(x=656,y=36,width=113,height=38)
        self.button_restart.pack()
        self.button_restart.place(x=829, y=544,width=122,height=40)
        self.button_back.pack()
        self.button_back.place(x=488, y=544,width=122,height=40)
        self.warning.pack()
        self.warning.place(x=590,y=130)
        self.guess_count = 0
        self.limit= int(math.log(100, 2))+1 if self.level.get() == "Easy" else int(math.log(250, 2))+1 if self.level.get() == "Medium" else int(math.log(1000, 2))+1
        self.random_number = random.randint(1, 100) if self.level.get() == "Easy" else random.randint(1, 250) if self.level.get() == "Medium" else random.randint(1, 1000)
        self.time_remaining = 30 if self.level.get() == "Easy" else 45 if self.level.get() == "Medium" else 60
        self.label_time_remaining["text"] = self.time_remaining
        self.running=True

        self.after(1000, self.countdown)
        self.warn()

        #Fonction de décompte du chrono
    def countdown(self):
        if self.running:
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.label_time_remaining["text"] = self.time_remaining
                self.after(1000, self.countdown)
            else:
                self.label_time_remaining["text"] = "Finished"
                messagebox.showinfo("Time's up!", "You ran out of time. The number was {}.".format(self.random_number))
                self.entry_answer.config(state="disabled")
                self.button_submit.config(state="disabled")
                
        #Fonction de validation de la valeur entrée par l'utilisateur
    def check_answer(self):
        user_answer = self.entry_answer.get()
        self.guess_count += 1
        if user_answer.isnumeric():
            user_answer = int(user_answer)
            if user_answer == self.random_number:
                self.running=False
                messagebox.showinfo("Congratulations!", f"You guessed the number correctly in {self.guess_count} chances and {self.time_remaining} seconds !")
                self.entry_answer.config(state="disabled")
                self.button_submit.config(state="disabled")
                self.after_cancel(self.after(1000,self.countdown))
            elif user_answer < self.random_number:
                messagebox.showinfo(f"Too low!", f"Try guessing a higher number.\n \n {self.limit-self.guess_count} chances left.")
            else:
                messagebox.showinfo("Too high!", f"Try guessing a lower number.\n \n {self.limit-self.guess_count} chances left.")
            if self.guess_count>= self.limit:
                self.running=False
                messagebox.showinfo("Limit of chance!", "You've chance the limit of chance. The number was {}.".format(self.random_number))
                self.entry_answer.config(state="disabled")
                self.button_submit.config(state="disabled")
                self.after_cancel(self.after(1000,self.countdown))

        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

        #Fonction de réinitialisation du jeu
    def restart_game(self):
        self.running=True
        self.after(1000, self.countdown)
        self.guess_count = 0
        self.limit= int(math.log(100, 2))+1 if self.level.get() == "Easy" else int(math.log(250, 2))+1 if self.level.get() == "Medium" else int(math.log(1000, 2))+1
        self.random_number = random.randint(1, 100) if self.level.get() == "Easy" else random.randint(1, 250) if self.level.get() == "Medium" else random.randint(1, 1000)
        self.time_remaining = 30 if self.level.get() == "Easy" else 45 if self.level.get() == "Medium" else 60
        self.label_time_remaining["text"] = self.time_remaining
        self.entry_answer.config(state="normal")
        self.button_submit.config(state="normal")
        self.entry_answer.delete(0, 'end')

        #Fonction qui permet de situer l'utilisateur sur la plage du nombre choisi
    def warn (self):
        if self.level.get() == "Easy":
            self.warning.config(text=f"I've chosen a number between 1 and 100. Try to Guess it. You've {self.limit} chances and 30 seconds")
        elif self.level.get() == "Medium":
            self.warning.config(text=f"I've chosen a number between 1 and 250. Try to Guess it. You've {self.limit} chances and 45 seconds")
        else:
            self.warning.config(text=f"I've chosen a number between 1 and 1000. Try to Guess it. You've {self.limit} chances and 60 seconds")



    def run(self):
        self.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()
