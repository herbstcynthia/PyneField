import random 


class Board:
    def __init__(self, n):
        self.size = n
        #Initialize the board
        self.board = [[0 for i in range(n)] for j in range(n)]
        #Generate the bombs
        for i in range(n):
            x = random.randint(0, n-1)
            y = random.randint(0,n-1)
            self.board[x][y] = 13 #I chose 13 to be the number for the bomb
        #Generate hints
        for i in range(n):
            for j in range(n):
                if self.board[i][j]== 13:
                    continue
                if i>0:
                    if j>0:
                        if self.board[i-1][j-1]==13:
                            self.board[i][j]+=1
                    if self.board[i-1][j]==13:
                        self.board[i][j]+=1
                    if j+1 < n:
                        if self.board[i-1][j+1] == 13:
                            self.board[i][j]+=1

                if j>0:
                    if self.board[i][j-1]==13:
                        self.board[i][j]+=1
                
                if j+1 < n:
                    if self.board[i][j+1]==13:
                        self.board[i][j]+=1
                if i+1 < n:
                    if j > 0:
                        if self.board[i+1][j-1]==13:
                            self.board[i][j]+=1
                    if self.board[i+1][j]==13:
                        self.board[i][j]+=1
                    if j+1 < n:
                        if self.board[i+1][j+1]==13:
                            self.board[i][j]+=1

    def Print(self):
        for i in self.board:
            for j in i:
                if j ==13:
                    print("*", end=' ')
                else:
                    print(j, end=' ')
            print()


def main():
    try:
        n = int(input("Choose Board Size:"))
    except:
        print("Size must be a number")
        return
    print(n, type(n))
    b = Board(n)
    b.Print()

main()
