import data
from question_model import Question
from quiz_brain import QuizBrain

QuestionBank = []
for question in data.question_data:
    Q_TEXT = question["text"]
    Q_ANSWER = question["answer"]
    new_question = Question(Q_TEXT, Q_ANSWER)
    # print(new_question.text)
    QuestionBank.append(new_question)


# print(QuestionBank)
quiz = QuizBrain(QuestionBank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.outro()
