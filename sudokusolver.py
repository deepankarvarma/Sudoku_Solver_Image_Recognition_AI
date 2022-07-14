from tkinter import Tk


rows, cols=9,9
def find(lst,searchEle):
    (i,j) = (-1, -1)
    for row in range(0,rows):
        for col in range(0,cols):
            if lst[row][col]==searchEle:
                (i,j) =(row,col)
                return (i,j)
    return (i,j)

def printSol(lst):
    print('\nSolution:')
    for row in lst:
        print(row) 

def sudokuSolver(lst):
    (i,j)=find(lst,0)
    if (i,j)==(-1,-1):
        printSol(lst)
        return
    excludedNums=set()
    for row in range(0,rows):
        for col in range(0,cols):
            if lst[row][col]!=0:
                if i==row or j==col or (i//3 ==row//3 and j//3==col//3):
                    excludedNums.add(lst[row][col])
    possibleNums=[1,2,3,4,5,6,7,8,9]
    for number in possibleNums:
        if number not in excludedNums:
            lst[i][j]=number
            sudokuSolver(lst)
            lst[i][j]=0

def main():
    root=Tk()
    root.title('Sudoku Solver using Image')
    root.iconbitmap('C:\\Users\\acer\\Desktop\\Thapar\\Subjects\\4th Semester\\Artificial Intelligence UCS411\\Project\\AI Project Deepankar Varma ,Prateek Sharawat\\logo.ico')
    root.geometry("400x400")
    # lst=eval(input('Enter the list (0 for missing values): '))
    lst=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
    sudokuSolver(lst)
    root.mainloop()

if __name__=='__main__':
    main()

