"""A class that can be used to represent Jeopardy game"""

class Jeopardy:

    def __init__(self):
        """Initialize attributes"""
        self.question = None
        self.answer = None
        self.curr_points = 0 # Points for a single question
        self.round = 1
        # Points for different teams
        self.team1 = 0
        self.team2 = 0
        self.team3 = 0
        self.team4 = 0

    """Getters"""
    def getTeam1Score(self):
        return self.team1

    def getTeam2Score(self):
        return self.team2

    def getTeam3Score(self):
        return self.team3

    def getTeam4Score(self):
        return self.team4

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getCurrPoints(self):
        return self.curr_points


    """Setters"""
    def updateQuestion(self, question):
        self.question = question

    def updateAnswer(self, answer):
        self.answer = answer

    def updateCurrPoints(self, points):
        self.curr_points = points

    def updateAll(self, question, answer, curr_points):
        self.question = question
        self.answer = answer
        self.curr_points = curr_points

    def addTeam1Points(self):
        self.team1 += self.curr_points

    def addTeam2Points(self):
        self.team2 += self.curr_points

    def addTeam3Points(self):
        self.team3 += self.curr_points

    def addTeam4Points(self):
        self.team4 += self.curr_points

    