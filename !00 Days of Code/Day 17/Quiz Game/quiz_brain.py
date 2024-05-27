class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.number_of_questions = len(question_list)
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].question} "
                            f"(True/False)?:").capitalize()
        right_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        self.check_answer(user_answer, right_answer)

    def still_has_question(self):
        return not self.question_number == self.number_of_questions

    def check_answer(self, u_ans, r_ans):
        if u_ans == r_ans:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {r_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
