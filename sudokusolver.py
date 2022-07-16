from ensurepip import bootstrap
from tkinter import END, Text, Tk, font
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk

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
    def close_win():
       root.destroy()
       main()
    def showimage():
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.")))
        if fln:
            lbl1.pack_forget()
            btn1.after(0, btn1.destroy)
            btn2.after(0, btn1.destroy)
            btn=Button(frm, text="Restart",command=close_win)
            btn.pack(side=tk.LEFT)
            btn=Button(frm, text="Solve",command=sudokuSolver(lst))
            btn.pack(side=tk.LEFT,padx=10)
            
            
        img=Image.open(fln)
        img.thumbnail((450,450))
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image=img   
    root=Tk()
    frm=tk.Frame(root)
    frm.pack()
    
    lbl=Label(root)
    lbl.pack()
    lbl1=Label(frm, text="",font= ('Helvetica',10))
    lbl1.pack(side=TOP,pady=0)
    lbl1=Label(frm, text="GUI Sudoku Solver",font= ('Helvetica',27))
    lbl1.pack(side=TOP)
    lbl1=Label(frm, text="",font= ('Helvetica',1))
    lbl1.pack(side=TOP)
    lbl1=Label(frm, text="Using Image",font= ('Helvetica',20))
    lbl1.pack(side=TOP)
    img = ImageTk.PhotoImage(Image.open("sudoku.png").resize((180,180)))
    lbl1=Label(frm, text="",image=img)
    lbl1.pack(side=TOP)
    
    btn1=Button(frm, text="Browse Image",bg="gray80",font= ('Helvetica',12),width=30,command=showimage)
    
    btn1.pack(side=BOTTOM,pady=3,padx=10)
    btn2=Button(frm, text="Exit",bg="gray80",font= ('Helvetica',12),width=30,command=lambda: exit())
    btn2.pack(side=BOTTOM,pady=10)

    root.title('Sudoku Solver using Image')
    root.iconbitmap('C:\\Users\\acer\\Desktop\\Thapar\\Subjects\\4th Semester\\Artificial Intelligence UCS411\\Project\\AI Project Deepankar Varma ,Prateek Sharawat\\logo.ico')
    root.geometry("400x400")

    lst=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
    root.mainloop()

if __name__=='__main__':
    main()

# # Import the required Libraries
# from tkinter import *
# from tkinter import ttk, filedialog
# from tkinter.filedialog import askopenfile

# # Create an instance of tkinter frame
# win = Tk()

# # Set the geometry of tkinter frame
# win.geometry("700x350")

# def open_file():
#    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
#    if file:
#       content = file.read()
#       file.close()
#       print("%d characters in this file" % len(content))

# # Add a Label widget
# label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
# label.pack(pady=10)

# # Create a Button
# ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

# win.mainloop()