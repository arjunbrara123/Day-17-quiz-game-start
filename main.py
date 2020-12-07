#Import libraries
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests

#Initialise variables
question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()
