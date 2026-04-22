import tkinter as tk
import random
import html


class QuizScreen(tk.Frame):
    def __init__(self, master, quiz_logic, answer_callback):
        super().__init__(master, bg="#1e1e2f")
        self.quiz_logic = quiz_logic
        self.answer_callback = answer_callback
        self.selected_answer = tk.StringVar()
        self.answer_buttons = []
        self.current_answers = []
        self.build_ui()

    def build_ui(self):
        self.question_label = tk.Label(
            self,
            text="",
            font=("Arial", 18, "bold"),
            wraplength=700,
            bg="#1e1e2f",
            fg="white",
            justify="center"
        )
        self.question_label.pack(pady=30)

        for _ in range(4):
            button = tk.Radiobutton(
                self,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 14),
                wraplength=600,
                bg="#2b2b40",
                fg="white",
                selectcolor="#444466",
                indicatoron=False,
                width=40,
                pady=10
            )
            button.pack(pady=8)
            self.answer_buttons.append(button)

        self.submit_button = tk.Button(
            self,
            text="Submit Answer",
            font=("Arial", 14),
            command=self.submit_answer
        )
        self.submit_button.pack(pady=20)

        self.score_label = tk.Label(
            self,
            text="Score: 0",
            font=("Arial", 12),
            bg="#1e1e2f",
            fg="white"
        )
        self.score_label.pack(pady=10)

    def load_question(self):
        question = self.quiz_logic.get_current_question()
        if not question:
            return

        self.selected_answer.set("")

        question_text = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in question["incorrect_answers"]]

        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        self.question_label.config(text=question_text)
        self.score_label.config(text=f"Score: {self.quiz_logic.score}")

        for i, button in enumerate(self.answer_buttons):
            button.config(text=answers[i], value=answers[i])

    def submit_answer(self):
        selected = self.selected_answer.get()
        if selected:
            self.answer_callback(selected)