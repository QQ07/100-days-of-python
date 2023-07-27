'''It will be the brain of our quiz app'''


class QuizBrain:
    '''It will be the brain of our quiz app'''

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        '''returns the boolean that specifies that are there any questions left'''
        if self.question_number < len(self.question_list):
            return True
        return False
    def next_question(self):
        '''Will return the next question of the quiz object'''
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number }. {question.text} (True/ False): ")
        # print(answer)
        answer= answer.lower()
        if answer == question.answer.lower():
            self.score += 1
            print(f"Correct🎉 Your Score is {self.score}")
        else:
            print(f"Uh Oh! Wrong Answer Current Score: {self.score}")

    def outro(self):
        '''Outro of the Quiz game'''
        print(f"\n\nGame Over Your Score: {self.score}" )
