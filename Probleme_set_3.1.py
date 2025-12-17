from copy import deepcopy
from probleme_set_3 import check_sudoku

def sudoku_grid_recursive(grid):
    #copy the grid (without modify the original)
    grid = deepcopy(grid)

    #search first empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                excluded = set()
                square_of_x = 3*(i//3)
                square_of_y = 3*(j//3)
                for k in range(9):
                    excluded.add(grid[i][k]) #row
                    excluded.add(grid[k][j]) #col
                    excluded.add(grid[square_of_x + k//3][ square_of_y + k % 3 ]) #sub-square of the grid
                
                for include_index in range(1, 10):
                    if include_index not in excluded:
                        grid[i][j] = include_index
                        success = sudoku_grid_recursive(grid)
                        if success: #sudoku valid
                            return success
                #no matched number      
                return False

    #the grid is complete if we don't find empty cell 
    return grid


from probleme_set_3 import ill_formed, valid, invalid, easy, hard

if __name__ == "__main__":
    print("Testing check_sudoku()")
    print(check_sudoku(ill_formed)) # --> None
    print(check_sudoku(valid))      # --> True
    print(check_sudoku(invalid))  # --> False
    print(check_sudoku(easy))      # --> True
    print(check_sudoku(hard))     # --> True
    
    
    
