"""Player construction 

An approach to OOP. We thought a good idea would be to organize the players in
specially hand made, organic player objects, which then are stored in a list.
Every Player is an instance of this class. 
"""

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 

class Player(object):
    """This is the beginning of the Class Player, which generates the obj."""

    def __init__(self, name, id, score=0):
        """Classic constructor.
        
        The name is self-explanatory. The id is used to differentiate between 
        the players. Logically there can be players with the same name, but
        the id cant be changed, it is fixed. 
        """

        self.name = name
        self.score = score
        self.id = id

    def printer(self):
        """A usefull procedure to print the instance information.""" 
        
        print("Name=", self.name, "Id=", self.id, "score=", self.score)

    def setscore(self, score):
        """Could be something so manipulate the score of a player."""
        
        self.score += score
    
    def getscore(self):
        """Setter and Getter are always kind of the same."""
        
        return (Self.score)
    
    def compare(self, other):
        """Approach of a comparator."""
        
        return self.score - other.score
