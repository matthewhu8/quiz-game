"""
This module defines the QuizBrain class, managing the quiz logic.
"""

import random


class QuizBrain:
    """Manages the quiz state and handles question flow."""

    def __init__(self, questions_list):
        """
        Initialize a new QuizBrain instance.

        Args:
            questions_list (list): A list of Question objects.
        """
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.total = 0

    def next_question(self):
        """Display the next question and gather user's answer."""
        print(f"Current Score: {self.score}")
        print(f"Questions remaining: {len(self.questions_list) - self.question_number}")

        current_question = self.questions_list[self.question_number]
        four_choices = [current_question.answer]
        four_choices.extend(current_question.options)
        random.shuffle(four_choices)

        user_answer = input(
            f"Q{self.question_number + 1}: {current_question.text} "
            "1 pt (type out answer): \n"
            f"A. {four_choices[0]}\n"
            f"B. {four_choices[1]}\n"
            f"C. {four_choices[2]}\n"
            f"D. {four_choices[3]}\n"
        )

        self.check_answer(user_answer, current_question.answer, score=1)

    def still_has_questions(self):
        """Check if there are more questions to be asked."""
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer, score):
        """
        Check if the user's answer is correct and update the score.

        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer for the question.
            score (int): The points awarded for a correct answer.
        """
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += score
        else:
            print(f"Incorrect! '{correct_answer}' was what we were looking for.")
            self.total += 1

        total_score = round((self.score / self.total) * 100, 2) if self.total > 0 else 100
        print(f"You are {total_score}% so far")
