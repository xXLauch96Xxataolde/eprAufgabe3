class Player(object):

    def __init__(self, name, id, score=0):
        self.name = name
        self.score = score
        self.id = id

    def printer(self):
        print("Name=",self.name,"Id=", self.id, "score=", self.score)

    def setscore(self, score):
        self.score += score
    
    def getscore(self):
        return (Self.score)
    
    def compare(self, other):
       return self.score - other.score