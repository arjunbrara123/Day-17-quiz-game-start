class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?:")
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
        print(f"Your score is {self.score}/{self.question_number+1}")

