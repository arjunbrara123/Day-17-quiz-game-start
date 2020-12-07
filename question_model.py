import random


class Question:
    def __init__(self, q_text, answer, choices):
        self.text = q_text
        self.answer = answer
        if type(choices) == 'str':
            self.choices[0] = choices
            self.choices.append(answer)
        elif choices[0] == 'True' or choices[0] == 'False':
            self.choices = ['True', 'False']
        else:
            self.choices = choices
            self.choices.append(answer)
            random.shuffle(self.choices)
