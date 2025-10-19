def isValidSudoku(board):
    #Check each Row
    checkRow(board)
    #Check column 

    #Check each block

    return 0

def checkRow(board):
    for i in range(9):
        print(board[i])
    return 0

def checkColumn(board):
    return 0

def checkBlock(board):
    return 0

def unit_tests():
    tests = [
        ([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]], True),
#    ([["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["4",".",".","8",".","3",".",".","1"]
#,["8",".",".",".","6",".",".",".","3"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]], False)
    ]
    case_number = 0
    for test in tests:
        case_number+=1
        my_var = isValidSudoku(test[0])
        if my_var == test[1]:
            print(f"Test Case: {case_number} has FAILED")
        else:
            print(f"Test Case: {case_number} has PASSED")

unit_tests()
