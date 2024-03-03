class Question:
    def __init__(self, questionId, tags, difficulty):
        self.question_id = questionId
        self.tags = tags
        self.difficulty= difficulty
        self.score = difficulty.value