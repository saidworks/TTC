from football import *
#inheritence is useful in handling exceptions
#example
def computeDivision(first,second):
    try:
        division = first/second
    except TypeError:
        print("You did not enter two floating point numbers!")
    except ZeroDivisionError:
        print("Don't give a zero for the second number")
    except:
        print("there was some other exception")
    else:
        return division

class MissingChildMethodError(Exception):
    pass
class footballPlayer(FootballPlayer):
    def isBad(self):
        raise MissingChildMethodError("Error! isBad is not defined")
player3 = footballPlayer('Ziko',"Zargos")
try:
    player3.isBad()
except MissingChildMethodError:
    print("Whoops! this method is not define ")

