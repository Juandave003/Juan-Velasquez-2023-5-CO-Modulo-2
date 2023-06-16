class ScoreTracker:
    def __init__(self):
        self.score = 0
        self.highest_score = 0
        self.death_count = 0

    def increase_score(self):
        self.score += 1

    def increase_death_count(self):
        self.death_count += 1

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

    def reset(self):
        self.score = 0
        self.death_count = 0
        self.highest_score = 0
