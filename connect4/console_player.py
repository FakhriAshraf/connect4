from .game import Grid, Player


class ConsolePlayer(Player):
    def play(self, grid: Grid) -> int:
        print(grid) # Affichage de la Grid
        chances = 3 # Initialisation des chances pour le joueur sur console
        while(chances !=0):
            chances -=1 # decrementation des chances
            column = int(input("Column value :")) #Lecture de la valeur de colonne
            if column <7 and column >=0: 
                return column
            else : print("Column value needs to be between 0 and 6 !!!\nYou still have ",chances," chances left")    
        

