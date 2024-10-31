from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = [Question(q) for q in question_data]
quiz = QuizBrain(question_bank)

quiz.still_has_questions()