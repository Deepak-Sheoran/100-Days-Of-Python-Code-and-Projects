from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for stuff in question_data:
    question_bank.append(Question(stuff['text'], stuff['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz!")
print(f"You final score was: {quiz.score}/{len(question_bank)}")
