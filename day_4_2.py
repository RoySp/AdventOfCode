#!/usr/bin/python3

class BingoCard:
    def __init__(self, grid):
        self.grid = grid

    def mark(self, value):
        for r in range(5):
            for c in range(5):
                if self.grid[r][c] == value:
                    #set marked
                    self.grid[r][c] = 'X'
                    return self.checkRow(r) or self.checkCol(c)
        return False

    def checkRow(self, r):
        return all(self.grid[r][c] == 'X' for c in range(5))

    def checkCol(self, c):
        return all(self.grid[r][c] == 'X' for r in range(5))

    def sum(self):
        return sum(val for row in self.grid for val in row if val != 'X')

filename = 'input/day4.txt'
with open(filename) as file:
    numbers = [int(n) for n in file.readline().split(',')]
    grids = []
    while file.readline():
        grids.append([[int(n) for n in file.readline().split()] for _ in range(5)])

last_win = False
cards = [BingoCard(grid) for grid in grids]
for number in numbers:
    for card in list(cards):
        if card.mark(number):
            cards.remove(card)
            last_win = number * card.sum()
print(last_win)