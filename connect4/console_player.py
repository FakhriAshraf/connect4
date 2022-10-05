from .game import Grid, Player


class ConsolePlayer(Player):
    def play(self, grid: Grid) -> int:
        print(grid)
        column = int(input("Column value :"))
        if column <7 and column >=0:
            return column
        

