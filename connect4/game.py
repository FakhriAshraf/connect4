from enum import Enum


class Cell(Enum):
    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    lines = 6
    columns = 7

    def __init__(self):
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    def place(self, column: int, cell: Cell) -> int:
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    def win(self, line: int, column: int) -> bool:
        adjacent = 0
        color = self.grid[line][column]
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0

        # TODO: Vertical
        adjacent = 0 # Reinitialiser la variable adjacent
        for ligne in range(Grid.lines):
            # boucler sur verticallement sur les cellules dans la meme colonne
            cell = self.grid[ligne][column] 
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0

        # TODO: Diagonal
        adjacent = 0
        #Verfication de la 1ere diagonnale 
        # GRID = """
        #|.......|
        #|...X...|
        #|..X....|
        #|.X.....|
        #|X......|
        # 0123456
        for l in range(Grid.lines):
            # Condition pour ne pas depasser les bordures de la Grid
            if (line - min(line,column) + l) < (Grid.lines) and (column - min(line,column) + l) < Grid.columns:   
                # Sur la diagonnale associee a la cellule actuelle, 
                # ou on commence par la premiere cell et 
                # on remonte en incrementant a la fois la ligne et la colonne  
                cell = self.grid[line - min(line,column) + l][column - min(line,column) + l]
                if cell == color:
                    adjacent += 1
                    if adjacent == 4:
                        return True
                else:
                    adjacent = 0     
        adjacent = 0
        #Verfication de la 2eme diagonnale 
        #|.......|
        #|O......|
        #|.O.....|
        #|..O....|
        #|...O...|
        # 0123456
        for l in range(Grid.lines):
                # Sur la diagonnale associee a la cellule actuelle, 
                # ou on commence par cette cell et 
                # on descend en incrementant la colonne et decrementant la ligne 
                # A vec une condition pour ne pas depasser les bordures de la Grid
            if (line - l) >= 0 and (column + l) < (Grid.columns):    
                cell = self.grid[line - l][column + l]
                if cell == color:
                    adjacent += 1
                    if adjacent == 4:
                        return True
                else:
                    adjacent = 0                                            
        return False

    def tie(self) -> bool:
        # TODO
        # Cherchant sur chaque ligne une cellule vide,
        # si on trouve une en retourne False sinon on boucle 
        # on retourne True si la Grid est pleine
        for line in range(Grid.lines):
            if Cell.EMPTY in self.grid[line]:
                return False
        return True


class Player:
    def play(self, grid: Grid) -> int:
        raise NotImplementedError


class Game:
    def __init__(self, player_a: Player, player_b: Player):
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B):
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
