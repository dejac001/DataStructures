Human = -1
Computer = 1

class Dummy:
    def __init__(self):
        pass

    def eval(self):
        return 0

    def goto(self, x, y):
        pass


class X(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.getscreen().register_shape("X", (
            (-40, -36), (-40, -44), (0, -4), (40, -44),
            (40, -36), (4, 0), (40, 36), (40, 44),
            (0, 4), (-40, 44), (-40, 36), (-4, 0),
            (-40, -36)
        ))
        self.shape("X")
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        return Computer


class O(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.shape('circle')
        self.penup()
        self.speed(5)
        self.goto(-100, -100)

    def eval(self):
        return Human


class Board:

    def __init__(self, board=None):
        """make a copy of the board. can be shallow copy because Turtle objects are immutable"""
        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if board is None:
                    rowlst.append(Dummy())
                else:
                    rowlst.append(board[i][j])
            self.items.append(rowlst)

    def __getitem__(self, item):
        return self.items[item]

    def __eq__(self, other):
        raise NotImplementedError

    def reset(self):
        screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100, -100)
                self.items[i][j] = Dummy()
        screen.tracer(0)

    def eval(self):
        """return an integer representing the state of the board.
        If the computer has won, return 1, if human has won, return -1, else return 0"""
        pass

    def full(self):
        """return true of board is completely filled up"""
        pass

    def drawXOs(self):
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col*100+50, row*100+50)
        screen.update()