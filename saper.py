import random
class Cell():
    def __init__(self, around_mines, mine) -> None:
        self.fl_open = False
        self.around_mines = around_mines
        self.mine = mine



class GamePole():
    def __init__(self, N, M) -> None:
        self.pole = GamePole.init(N, M)


    def _count_mines(sheme, i, j):
        res = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if (k or l) and (-1 < i + k < len(sheme)) and (-1 < j + l < len(sheme)):
                    res += sheme[i + k][l + j]
        return res


    def init(N, M):
        pole = []

        mine_index_lst = [[x//N, x%N] for x in random.sample(range(N**2), M)]
        sheme = [[0]*N for _ in range(N)]
        for pair in mine_index_lst:
            sheme[pair[0]][pair[1]] = 1

        for i, row in enumerate(sheme):
            row_obj = []
            for j, x in enumerate(row):
                cell = Cell(GamePole._count_mines(sheme, i, j), x)
                row_obj.append(cell)
            pole.append(row_obj)
        return pole
    

    def show(self):
        for row in self.pole:
            for x in row:
                print(x.around_mines if x.fl_open else '#', end = ' ')
            print()
        
    def show_mines(self): 
        for row in self.pole:
            for x in row:
                print(x.mine, end = ' ')
            print()
    


pole_game = GamePole(10, 12)
print(isinstance(pole_game, GamePole))
#assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')

