from models import (HackathonProcess, Question, Difficulty, Users)
hackathon = HackathonProcess

q1 = Question(1, ["ds_algo","hudi"], Difficulty.EASY)
q2 = Question(2, ["ds_algo", "trie"], Difficulty.MEDIUM)

hackathon.add_question(q1)
hackathon.add_question(q2)


user1 = Users(1, "Alice")
user2 = Users(2, "Bob")

user1.solve(q1)
user1.solve(q2)

hackathon.display_leaderboard('user')