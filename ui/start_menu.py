import tkinter as tk


class StartMenu(tk.Frame):
    def __init__(self, master, start_callback):
        super().__init__(master, bg="#1e1e2f")
        self.start_callback = start_callback
        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self,
            text="Welcome to the API Quiz Game",
            font=("Arial", 24, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=40)

        start_button = tk.Button(
            self,
            text="Start Quiz",
            font=("Arial", 16),
            command=self.start_callback,
            width=15
        )
        start_button.pack(pady=20)