from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#B1DDC6"
RED = "#db4040"
GREEN = "#6bd962"
FONT = ("Arial",18,"normal")

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        #window init
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,background=THEME_COLOR)
        #label init
        self.score_label = Label(text="score:0",background=THEME_COLOR,font=("Arial",12,"normal"))
        self.score_label.grid(column=1,row=0,)
        self.canvas = Canvas()
        self.canvas.config(height= 250, width=300,borderwidth=0,highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="question here", font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        #buttons init
        self.RIGHT = PhotoImage(file="images/right.png")
        self.WRONGE = PhotoImage(file="images/wrong.png")
        self.right = Button(image=self.RIGHT,borderwidth=0,height=100,width=100,highlightthickness=0,activebackground=THEME_COLOR,background=THEME_COLOR,command=self.true)
        self.right.grid(column=0,row=2)
        self.wronge = Button(image=self.WRONGE,borderwidth=0,height=100,width=100,highlightthickness=0,activebackground=THEME_COLOR,background=THEME_COLOR,command=self.false)
        self.wronge.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text = q_text)
            self.score_label.config(text=f"Score:{self.quiz.score}/20")
        else:
            self.canvas.itemconfig(self.question,text ="You've completed the quiz")
            self.right.config(state="disabled")
            self.wronge.config(state="disabled")
    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))




    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, func=self.get_next_question)










