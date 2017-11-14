class Player(object):

    def __init__(self, name, id, score=0, dice_roll_counter=0):
        self.name = name
        self.score = score
        self.dice_roll_counter = dice_roll_counter
        self.id = id

    def pri(self):
        print("New Obj", self.name)

    def setscore(self, score):
        self.score += score
    
    def getscore(self):
        return (Self.score)
    
    def compare(self, other):
       return self.score - other.score