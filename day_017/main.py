from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = [Question(q) for q in question_data]
quiz = QuizBrain(question_bank)

def main():
    quiz.still_has_questions()

if __name__ == "__main__":
    main()