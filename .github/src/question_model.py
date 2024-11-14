"""
This module defines the Question class, representing a trivia question.
"""


class Question:
    """A class representing a trivia question."""

    def __init__(self, question_text, answer_text, points, options):
        """
        Initialize a new Question instance.

        Args:
            question_text (str): The text of the question.
            answer_text (str): The correct answer.
            points (int): Points awarded for a correct answer.
            options (list): List of possible answers.
        """
        self.question_text = question_text
        self.answer_text = answer_text
        self.points = points
        self.options = options
