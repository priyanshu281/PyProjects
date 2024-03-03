class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.solved_problems= set()

    def solve(self, problem): #shouldnt be part of this
        self.solved_problems.add(problem)

    def get_total_score(self):
        total_score= 0
        for problem in self.solved_problems:
            total_score += problem.score
        return total_score
#solutions class