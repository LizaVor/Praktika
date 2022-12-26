class Queen:
    def __init__(self,N): 
        self.N=N
        self.board=[[0 for i in range(N)]for j in range(N)]
        self.find_sol(self.board, 0)


    def get_result(self):
        return self.board


    def check_brd(self,board,i,j):
        for x in range(i):
            if board[x][j]==1:
                return False
        for x,y in zip (range(i,-1,-1),range(j,self.N,+1)):
            if board[x][y]==1:
                return False    
        for x,y in zip (range(i,-1,-1),range(j,-1,-1)):
            if board[x][y]==1:
                return False
        return True


    def find_sol(self,board,col):
        if col>=self.N:
            return True

        for i in range(self.N):
            if self.check_brd(board,col,i):
                board[col][i]=1
                if self.find_sol(board,col+1):
                    return True
                board[col][i]=0
        return False
