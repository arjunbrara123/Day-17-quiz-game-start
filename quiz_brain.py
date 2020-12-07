import json
import requests

from question_model import Question


class QuizBrain:

    def __init__(self, q_list):
        """Generate random question list from Open Trivia API"""
        # Set initial class variables
        self.question_number = 0
        self.score = 0
        self.question_list = []

        # Ask user for desired question set up and format
        diff = input("Pick a difficulty (hard/medium/easy):").lower()
        if diff != "hard" and diff != "medium":
            diff = "easy"
        try:
            q_count = int(input("How many questions do you want? (1-10):"))
            if q_count > 10 or q_count < 2:
                q_count = 10
        except ValueError:
            q_count = 3

        # Use JSON API to pull random questions from internet
        self.json_bank = (
            requests.get("https://opentdb.com/api.php?amount=" + str(
                q_count) + "&category=18&difficulty=" + diff + "&type=multiple"))
        if self.json_bank.status_code != 200:
            print("ERROR: Couldn't establish an internet connection to remote server. "
                  "Using default questions bank instead")
            self.question_list = q_list
        else:
            # Get api string
            api_bank = json.loads(self.json_bank.text)['results']
            for i in range(len(api_bank)):
                d_question = dict(api_bank[i])
                i_question = Question(d_question["question"], d_question["correct_answer"],
                                      d_question["incorrect_answers"])
                self.question_list.append(i_question)

    def next_question(self):
        """Ask user the next question and check if their answer is correct"""
        user_answer = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
            f"({self.question_list[self.question_number].choices}) :")
        correct_answer = self.question_list[self.question_number].answer
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def still_has_questions(self):
        """Check if there are still unasked questions remaining in the bank"""
        if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your final score was {self.score}")
            return False
        elif self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        """Check if user answer is correct"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Well done! The answer is '{correct_answer}'! "
                  f"Your score is {self.score}/{self.question_number+1}")
        else:
            print(f"Nope - the correct answer is '{correct_answer}'. "
                  f"Your score is {self.score}/{self.question_number+1}")
