class QuizLogic:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
        self.score = 0

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def check_answer(self, selected_answer):
        current_question = self.get_current_question()
        if not current_question:
            return False

        correct = selected_answer == current_question["correct_answer"]
        if correct:
            self.score += 1

        self.current_index += 1
        return correct

    def has_more_questions(self):
        return self.current_index < len(self.questions)