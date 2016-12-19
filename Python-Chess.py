import unittest
#Used for position on chess board. X can be 0-7 legally (a-h on board)
#Y can be 0-7 legally (1-8 on board)
class Position:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def to_string(self):
		return "({0}, {1})".format(self.x, self.y)


class Piece:

	#All pieces have a position, and whether or not they are white or not.
	#Pieces are defaulted to White, and position (0,0) == a1
	def __init__(self, pos=Position(), isWhite=True):
		self.pos = pos
		self.isWhite = isWhite

	def to_string(self):
		return "Position: {0}, White: {1}".format(self.pos.to_string(), self.isWhite)

#Class pawn is a piece, inherits from it so that it can use its pos and isWhite.
class Pawn(Piece):

	def __init__(self, pos=Position(), isWhite=True):
		super().__init__(pos, isWhite)

	#Gets all the possible moves of a pawn based on its current position
	def getPossibleMoves(self):
		moves = []
		if(self.pos.x > 0):
			takeLeft = Position(self.pos.x - 1, self.pos.y + 1)
			moves.append(takeLeft)
		forwards = Position(self.pos.x, self.pos.y + 1)
		moves.append(forwards)
		if(self.pos.x < 7):
			takeRight = Position(self.pos.x + 1, self.pos.y + 1)
			moves.append(takeRight)
		return moves



#class Board:

	#Board will contain a dictionary of Position -> Piece for both black and white. This will be useful in finding out whether or not a piece can move to a position.

class TestPawnMethods(unittest.TestCase):

    def test_pawn_get_possible_moves_no_left(self):
    	'''
    	pawn = Pawn()
    	moves = pawn.getPossibleMoves()
    	expected_moves = []
    	expected_moves.append(Position(0, 1))
    	expected_moves.append(Position(1, 1))
    	self.assertEqual(moves, expected_moves)
    	'''
    	pos1 = Position()
    	pos2 = Position()
    	self.assertEqual(pos1, pos2)
        

if __name__ == '__main__':
    unittest.main()