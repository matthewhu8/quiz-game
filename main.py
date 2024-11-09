from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    quiz_question = q["text"]
    quiz_answer = q["answer"]
    new_question = Question(quiz_question, quiz_answer, 1)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.question_number += 1

print ("You've completed the quiz")
print (f"Your final score: {round((quiz.score/quiz.question_number)*100, 2)}%")