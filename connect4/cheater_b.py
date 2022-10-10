from .game import Grid, Player, Cell

# Ici, on cherche une cellule vide, et on replis 3 cellules
# on reteorne le numéro de la colonne pour remplis la 4eme pour gagner 
class CheaterB(Player):
    def play(self, grid: Grid) -> int:
        for line in range(grid.lines):
            for column in range(grid.columns):
                if grid.grid[line][column] == Cell.EMPTY:
                    for l in range(3):
                        grid.grid[line+l][column] = Cell.B
                    return column
