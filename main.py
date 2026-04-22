import tkinter as tk
from tkinter import messagebox

from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from api.trivia_api import get_questions
from game.quiz_logic import QuizLogic
from ui.start_menu import StartMenu
from ui.quiz_screen import QuizScreen
from ui.results_screen import ResultsScreen


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.current_screen = None
        self.quiz_logic = None

        self.show_start_menu()

    def clear_screen(self):
        if self.current_screen is not None:
            self.current_screen.destroy()

    def show_start_menu(self):
        self.clear_screen()
        self.current_screen = StartMenu(self.root, self.start_quiz)
        self.current_screen.pack(fill="both", expand=True)

    def start_quiz(self):
        try:
            questions = get_questions()
            self.quiz_logic = QuizLogic(questions)
            self.show_quiz_screen()
        except Exception as error:
            messagebox.showerror("Error", f"Failed to load quiz questions.\n{error}")

    def show_quiz_screen(self):
        self.clear_screen()
        self.current_screen = QuizScreen(self.root, self.quiz_logic, self.submit_answer)
        self.current_screen.pack(fill="both", expand=True)
        self.current_screen.load_question()

    def submit_answer(self, selected_answer):
        self.quiz_logic.check_answer(selected_answer)

        if self.quiz_logic.has_more_questions():
            self.current_screen.load_question()
        else:
            self.show_results_screen()

    def show_results_screen(self):
        self.clear_screen()
        self.current_screen = ResultsScreen(
            self.root,
            self.quiz_logic.score,
            len(self.quiz_logic.questions),
            self.show_start_menu
        )
        self.current_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()