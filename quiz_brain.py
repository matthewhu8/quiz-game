class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.total = 0
    def next_question(self):
        print(f"Current Score: {self.score}")
        print(f"Questions remaining: {len(self.questions_list) - self.question_number}")
        current_question = self.questions_list[self.question_number]

        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} 1 pt (true/false): ")
        self.check_answer(user_answer, current_question.answer, current_question.score)
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, answer, score):
        if user_answer.lower() == answer.lower():
            print("Correct!")
            self.score += score
            self.total += 1
        else:
            print(f"Incorrect! '{answer}' was what we were looking for.")
            self.total += 1

        total_score = round((self.score / self.total)*100, 2)
        print(f"You are {total_score}% so far")



