from .game import Cell, Grid


def serialize_cell(cell: Cell) -> str:
    # Comparer la valeur de cellule et retouner le code ASCII associe a son caractere 
    if cell == Cell.EMPTY :
        return str(ord("."))
    if cell == Cell.A :
        return str(ord("X"))
    if cell == Cell.B :
        return str(ord("O"))


def deserialize_cell(cell: str) -> Cell:
    # retourner le caractere de cellule en comparant la valeur cell avec le code ASCII associe
    if cell == str(ord(".")) :
        return Cell.EMPTY
    if cell == str(ord("X")) :
        return Cell.A
    if cell == str(ord("O")) :
        return Cell.B        


def serialize_grid(grid: Grid) -> str:
    for line in range(grid.lines):
        for column in range(grid.columns):
            grid.grid[line][column] =serialize_cell(grid.grid[line][column]) 
    return grid   


def deserialize_grid(grid: str) -> Grid:
    for line in range(grid.lines):
        for column in range(grid.columns):
            grid.grid[line][column] = deserialize_cell(grid.grid[line][column])       
    return grid   
