result = []
 
def isSafe(board, row, col):
 
    
    for i in range(col):
        if (board[row][i]):
            return False
 
    
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
 
    
    i = row
    j = col
    while j >= 0 and i < n:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True
 
def solveNQUtil(board, col):
    
    if (col == n):
        v = []
        for i in board:
          for j in range(len(i)):
            if i[j] == 1:
              v.append(j+1)
        result.append(v)
        return True
 
    
    res = False
    for i in range(n):
 
        
        if (isSafe(board, i, col)):
 
            
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0  
 
    
    return res
  
def solveNQ(n):
    result.clear()
    board = [[0 for j in range(n)]
             for i in range(n)]
    solveNQUtil(board, 0)
    result.sort()
    return result
 
 
n = int(input("Enter the value of n: "))
print("Every index states the position of the nth queen")
print("All possible solutions of %d-queens problem are : "%n)

res = solveNQ(n)
for i in res:
	print("\n",i)