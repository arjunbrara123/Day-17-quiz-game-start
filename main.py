# Import libraries
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Initialise variables
question_bank = []

# Default questions to fall back on if unable to generate random questions
for item in question_data:
    pass
    #question = Question(item["text"], item["answer"], "True/False")
    #question_bank.append(question)

# Setup quiz questions
qb = QuizBrain(question_bank)

# While questions remaining, keep asking quiz questions
while qb.still_has_questions():
    qb.next_question()
