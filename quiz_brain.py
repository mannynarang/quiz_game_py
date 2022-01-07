
class Quiz:

    def __init__(self, questions):
        """takes in list of questions"""
        self.questions_list = questions
        self.current_question = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.current_question]
        self.current_question += 1
        user_answer = input(f"Q.{self.current_question} : {current_question.text} (True/False) : ").lower()
        if self.is_correct(user_answer):
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry no! The correct answer is {self.questions_list[self.current_question-1].answer} ")
        print(f"You current score is :  {self.score}/{self.current_question}")

    def still_as_questions(self):
        return self.current_question < len(self.questions_list)

    def is_correct(self, answer):
        """returns true if answer is correct to the current question"""
        current_answer = self.questions_list[self.current_question-1].answer.lower()
        return current_answer == answer

