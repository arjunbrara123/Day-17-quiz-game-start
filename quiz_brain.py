class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def nextQuestion(self):
        usrAns = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?:")
