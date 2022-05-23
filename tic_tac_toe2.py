## player.py - basic info of player
## game.py - take care of user states, utilise grid.py and player.py
## grid.py - take care of its own state i.e what is current state, valid or not, win or not, draw, etc - DONE


class Player:
    def __init__(self, playerName):
        self.username = playerName


class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(0, 3)] for _ in range(0, 3)]

    def printGrid(self):
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                print(self.grid[y][x], end=" ")
            print("")

    def setValue(self, y, x, param):
        self.grid[y][x] = param

    ## solving tic tac toe
    def solve(self):
        # horizontals
        for y in range(0, len(self.grid)):
            state = self.grid[y][0]
            Flag = True
            if (state == 0):
                continue
            for x in range(1, len(self.grid[y])):
                if (state != self.grid[y][x]):
                    Flag = False
            if (Flag):
                return True

        # verticals
        for x in range(0, len(self.grid[0])):
            state = self.grid[0][x]
            Flag = True
            if (state == 0):
                continue
            for y in range(1, len(self.grid[0])):
                if (state != self.grid[y][x]):
                    Flag = False
            if (Flag):
                return True

        # diagonals
        if (self.grid[1][1] != 0 and self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]):
            return True
        if (self.grid[1][1] != 0 and self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]):
            return True

        # no one won
        return False

    # Any more possible moves are left or not - check for draw
    def isValid(self):
        # if everything filled then no more possible
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[0])):
                if (self.grid[y][x] == 0):
                    return True
        return False

    # Valid move check for a position by user
    def validMove(self, y, x):
        if (self.grid[y][x] != 0):
            return False
        return True


class Game:
    def __init__(self, user1, user2):
        self.player1 = user1
        self.player2 = user2
        self.choice = True  # True shows player1 has chance to go first
        self.grid = Grid()

    def gameInstance(self):
        self.grid.printGrid()

    def play(self):
        if (not self.grid.isValid()):
            print("DRAW")
            return
        if (self.choice):
            print("Player 1: " + self.player1.username + " Move")
            play1Y, play1X = list(map(int, input().strip().split()))
            if (self.grid.validMove(play1Y, play1X)):
                self.grid.setValue(play1Y, play1X, 1)
                self.gameInstance()
                if (self.grid.solve()):
                    print("Player 1:" + self.player1.username + " Won")
                    return
                self.choice = False
                self.play()
            else:
                print("Invalid Move")
                self.play()
        else:
            print("Player 2: " + self.player2.username + " Move")
            play2Y, play2X = list(map(int, input().strip().split()))
            if (self.grid.validMove(play2Y, play2X)):
                self.grid.setValue(play2Y, play2X, 2)
                self.gameInstance()
                if (self.grid.solve()):
                    print("Player 2:" + self.player2.username + " Won")
                    return
                self.choice = True
                self.play()
            else:
                print("Invalid Move")
                self.play()


def tic_tac_toe2():
    player1 = Player("userName1")
    player2 = Player("userName2")
    newGame = Game(player1, player2)
    newGame.gameInstance()
    newGame.play()
