class Hackathon:
    def __init__(self):
        self.questions = {}
        self.users= {}
    def add_question(self, question):
        self.questions[question.question_id] = question

    def fetch_problems(self, tags= None, difficulty= None):
        if tags is None and difficulty is None:
            return list(self.questions.values())

        filteredProblems = [question for question in self.questions.values() if
                            (not tags or set(tags).intersection(question.tags)) and
                            (not difficulty or question.difficulty == difficulty)]

        return filteredProblems

    def add_user(self, user):
        self.users[user.user_id] = user

    def display_leaderboard(self, flag , n=5):
        if flag == 'user':
            leaderboard = sorted(self.users.values(), key= lambda user: user.get_total_score(), reverse= True)[:n]
            print("Top Users:")
            for i , user in enumerate(leaderboard, 1):
                print(f"{i}. {user.name}: {user.get_total_score() } points")
        elif flag == 'department':
            department_scores = {}
            for user in self.users.values():
                department = user.department
                if department not in department_scores:
                    department_scores[department] = 0
                department_scores[department] += user.get_total_score()
                sorted_departments = sorted(department_scores.items(), key= lambda user: user.get_total_score, reverse=True)[:n]
                print("Top departments:")
                for (department, score) in enumerate(sorted_departments):
                    print(f"{department}: {score} points")
        else:
            print("Invalid flag")
#orielly head first design patterns ,




