class Board:
    def __init__(self, n):
        self.size = n
        self.board = [[0 for i in range(n)] for j in range(n)]
    def Print(self):
        print(self.board)


def geraTabuleiro(n):
    print("gerando o tabuleiro")
    

def printTabuleiro():
    print("printando")

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
