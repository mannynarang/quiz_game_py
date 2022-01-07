from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for questions in question_data:
    question = Question(questions['question'], questions['correct_answer'])
    question_bank.append(question)

quiz = Quiz(question_bank)
while quiz.still_as_questions():
    quiz.next_question()
    print("\n")

print("You have completed the quiz")
print(f"Your final score was  {quiz.score} / {quiz.current_question}")

