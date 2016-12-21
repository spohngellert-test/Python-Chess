import unittest
#Used for position on chess board. X can be 0-7 legally (a-h on board)
#Y can be 0-7 legally (1-8 on board)
class Position:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def to_string(self):
		return "({0}, {1})".format(self.x, self.y)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__


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
	def getAllMoves(self):
		moves = []
		y_factor = 1
		if not self.isWhite:
			y_factor = -1
		#Checking for whether pawn is on left side of board
		if(self.pos.x > 0):
			takeLeft = Position(self.pos.x - 1, self.pos.y + y_factor)
			moves.append(takeLeft)
		#Straight forwards
		forwards = Position(self.pos.x, self.pos.y + y_factor)
		moves.append(forwards)
		#Move forwards 2
		if((self.pos.y == 1 and self.isWhite) or (self.pos.y == 6 and (not self.isWhite))):
			forwards_two = Position(self.pos.x, self.pos.y + (y_factor * 2))
			moves.append(forwards_two)
		#Checking whether pawn is on right side of board
		if(self.pos.x < 7):
			takeRight = Position(self.pos.x + 1, self.pos.y + y_factor)
			moves.append(takeRight)
		return moves



#class Board:

	#Board will contain a dictionary of Position -> Piece for both black and white. This will be useful in finding out whether or not a piece can move to a position.

class TestPawnMethods(unittest.TestCase):

    def test_pawn_get_possible_moves_no_left(self):
    	pawn = Pawn()
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(0, 1))
    	expected_moves.append(Position(1, 1))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_no_right(self):
    	pawn = Pawn(Position(7, 2))
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(6, 3))
    	expected_moves.append(Position(7, 3))
    	self.assertListEqual(moves, expected_moves)

    def test_pawn_get_possible_moves_both(self):
    	pawn = Pawn(Position(5, 4))
    	moves = pawn.getAllMoves()
    	expected_moves = []
    	expected_moves.append(Position(4, 5))
    	expected_moves.append(Position(5, 5))
    	expected_moves.append(Position(6, 5))
    	self.assertListEqual(moves, expected_moves)

        

if __name__ == '__main__':
    unittest.main()