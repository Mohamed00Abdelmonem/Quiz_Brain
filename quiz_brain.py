
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.your_score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_q(self):
        current_questioin = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number + 1}: {current_questioin.text} (True/False): ")
        self.check_answer(user_answer, current_questioin.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You go it right.")
            self.your_score += 1
        else:
            print("That's Wrong.")

        print(f"The correct answer was: {user_answer}. ")

        print(f"your score = {self.question_number}/{self.your_score}")
        print("\n")
