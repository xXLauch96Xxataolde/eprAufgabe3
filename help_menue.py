"""Just for opening a txt file and printing its content to teh console."""

__author__ = "6770541: Niels Heissel, 6785468: Robert am Wege"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "" 
__email__ = "uni.goethe.horde@gmail.com" 


def helpings():
    """Procedure for opening a file and printing it to the console."""
    
    f = open("menue.txt", "r")

    print(f.read(10000))
    print("\n")
    print(f.read())
