import requests
from question_model import Question

class QuizBrain:

    def __init__(self, q_list):

        #Set initial class variables
        self.question_number = 0
        self.score = 0
        self.question_list = []

        #Ask user for question set up and format
        diff = input("Pick a difficulty (hard/medium/easy) :").lower()
        if diff != "hard" and diff != "medium":
            diff = "easy"
        q_count = int(input("How many questions do you want? (1-10) :"))
        if q_count > 10 or q_count < 2:
            q_count = 10

        #Use JSON API to pull random questions from internet
        self.json_bank = (
            requests.get("https://opentdb.com/api.php?amount=" + str(q_count) + "&category=18&difficulty=" + diff))
        if self.json_bank.status_code != 200:
            print("ERROR: Couldn't establish an internet connection to remote server. "
                  "Using default questions bank instead")
            self.question_list = q_list
        else:
            #Get api string
            api_text = self.json_bank.text.replace('{"response_code":0,"results":[{', '[{')
            api_text = api_text[0:-1]
            api_bank = eval(api_text)
            for i in range(len(api_bank)):
                self.question_list.append(Question(dict(api_bank[i])["question"], dict(api_bank[i])["correct_answer"]))

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}:")
        correct_answer = self.question_list[self.question_number].answer
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was {self.score}")
            return False
        elif self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print("The correct answer is: " + correct_answer)
        print(f"Your score is {self.score}/{self.question_number + 1}")
