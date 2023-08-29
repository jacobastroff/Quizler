THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
class UserInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_text = Label(text="Score: 0", fg="white", bg = THEME_COLOR)
        self.score_text.grid(row=1, column = 2)
        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0, highlightbackground=THEME_COLOR)
        self.question_text= self.canvas.create_text(150, 125, width = 280, text="Some question text", font=('Arial', 20, 'italic'))
        self.canvas.grid(row=2, column =1, columnspan=2, pady=50 )
        self.correct_image = PhotoImage(file='images/true.png')
        self.wrong_image = PhotoImage(file='images/false.png')
        self.correct_btn = Button(image=self.correct_image, highlightbackground=THEME_COLOR, highlightthickness=0,command=self.check_answer_correct)
        self.correct_btn.grid(column = 1, row = 3)
        self.false_btn = Button(image = self.wrong_image,highlightbackground=THEME_COLOR, highlightthickness=0, command=self.check_answer_false)
        self.false_btn.grid(row= 3, column = 2)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.false_btn.config(state="disabled")
            self.correct_btn.config(state="disabled")
    def check_answer_correct(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right =self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def change_background_canvas(self,bgcolor):
        self.canvas.configure(bg=bgcolor)

    def give_feedback(self, is_right_answer):
        if(is_right_answer):
            bgcolor = 'green'
        else:
            bgcolor= 'red'
        print(bgcolor)
        self.change_background_canvas(bgcolor)
        self.window.after(1000, self.get_next_question)





