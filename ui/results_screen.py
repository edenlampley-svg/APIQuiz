import tkinter as tk


class ResultsScreen(tk.Frame):
    def __init__(self, master, score, total_questions, restart_callback):
        super().__init__(master, bg="#1e1e2f")
        self.score = score
        self.total_questions = total_questions
        self.restart_callback = restart_callback
        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self,
            text="Quiz Complete!",
            font=("Arial", 24, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=40)

        score_label = tk.Label(
            self,
            text=f"Your Score: {self.score} / {self.total_questions}",
            font=("Arial", 18),
            bg="#1e1e2f",
            fg="white"
        )
        score_label.pack(pady=20)

        restart_button = tk.Button(
            self,
            text="Play Again",
            font=("Arial", 14),
            command=self.restart_callback,
            width=15
        )
        restart_button.pack(pady=20)