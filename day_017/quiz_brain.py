class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        while self.question_number < len(self.question_list):
            print(f"Your current score is {self.score}")
            self.ask_question()

        print(f"Your final score is {self.score}/{len(self.question_list)}")

    def next_question(self):
        try:
            self.question_number += 1
        except Exception:
            print("Out of Questions!")

    def ask_question(self):
        if input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}\nTrue or False\n").lower() == self.question_list[self.question_number].answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect or invalid input.\n")

        self.next_question()