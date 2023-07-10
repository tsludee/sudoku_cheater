def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> -1
    # return row, col tuple (or (None, None) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None # if no spaces inthe puzzle are empty


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess is valid
    #returns true if is valid, false otherwise
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # now for columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    #now for the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # if we get here, these checks pass
    return True



def solve_sudoku(puzzle):
    #solve sudoku using a backtracking technique
    # the puzzle is a list of lists each inner list is a row

    #step 1 - find an empty place on the list
    row, col = find_next_empty(puzzle)
    
    # step 1.1: if there's nowhere left, we're done
    if row is None:
        return True
    
    # step 2: if there's a place for the guess, we want to make a guess and try them all until one works
    for guess in range(1, 10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid or if guess does not solve the puzzle, then we need to backtrack
        #backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess
    # step 6: if none of the numbers that we try work, this puzzle is FALSE
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,    7, 1, 9,    -1, 8, -1],

        [-1, 5, -1, -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,    -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1,  1, -1, 5,   -1, 4, -1],
        [1, -1, 9,  -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)