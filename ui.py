from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 12))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            text='Quizzler'
        )

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)

        self.true_button.grid(row=2, column=1)
        self.false_button.grid(row=2, column=0)

        self.show_next_question()

        self.window.mainloop()

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def show_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.score_label['text'] = f'Score: {self.quiz.score}'
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.show_next_question)
