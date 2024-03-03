import unittest
from enum import Enum
from models import HackathonProcess, Difficulty, Question, Users
class TestHackathonSystem(unittest.TestCase):
    def setUp(self):
        self.hackathon_system = HackathonProcess()

    def test_add_question(self):
        question = Question(1, ["ds_algo", "hudi"], Difficulty.EASY)
        self.hackathon_system.add_question(question)
        self.assertIn(question, self.hackathon_system.questions.values())


if __name__ == '__main__':
    unittest.main()
