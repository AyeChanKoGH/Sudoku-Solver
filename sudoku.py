''''
sudoku backtracking Algorithm with tkinter GUI
--you can play any sudoku problem to get valid sudoku problem
--backtracking Algorithm is a kind of recurrive Algorithm
**To Notice is backtracking is a recurive algorithm and still work after finding the solution until the stack back
**For too many time changing the screen,you need to update the tkinter window
    #####                
                    Backtracking
    Backtracking is a general algorithm for finding all(or some) solution
    to some computational problems, notably constraint satisfaction problem,
    that incrementally builds candidate("Backtracks") as soon as it determines that 
    the candidate cannot possibly be completed to avoid solution.
                                                    Wikipedia
                                                    ##########
########'' For complete my project thank for Stack Overflow, YouTuber, and many website''
'''
###### First we need to import the require packages
from tkinter import Tk,messagebox, Canvas,TOP,Button,PhotoImage
import time
SIDE=50                         #for one square size
MERGIN=2                        #Margin from tkinter window to canvas screen
HEIGHT=WIDTH=MERGIN*2+ SIDE*9   #To create fine screen
#Creating sudoku class with UI and the back end solution
class sudoku():
    def __init__(self):
        self.window=Tk()                    #creating Tk(window)
        self.row,self.col=0,0
        self.__createUI()
        self.mainarr=[[0]*9 for i in [0]*9] #main array to solve
        self.__clarr=[[0]*9 for i in [0]*9]
        self.num=[[0]*9 for i in [0]*9]     #for event write in canvas window
        self.count=True                        #to escape backtracking recursive
        
    def __createUI(self):
        self.window.title("Sudoku Solve")
        try:
            self.p1=PhotoImage(file='sudoku.png')
            self.window.iconphoto(False,self.p1)
        except:
            pass
        self.canvas1=Canvas(self.window,width=WIDTH,height=HEIGHT)
        self.canvas1.pack(padx=9,pady=9)
        self.canvas2=Canvas(self.window,width=WIDTH,height=20)
        self.canvas2.pack(padx=9,pady=9)
        self.btn_solve=Button(self.canvas2,text="Solve Puzzles",width=30,height=2,bg='green',command=self.__solve)
        self.btn_solve.pack(padx=9,pady=9)
        self.btn_clear=Button(self.canvas2,text="Clear Puzzles",width=30,height=2,bg='green',command=self.__clearalltext)
        self.btn_clear.pack(padx=9,pady=9)
        self.__drawgrid()

    ############# For line grid #############
    def __drawgrid(self):
        for i in range(10):
            color='blue' if i%3==0 else 'gray'
            lwidth=3 if i%3==0 else 1
            x0=MERGIN+i*SIDE
            x1=MERGIN+i*SIDE
            y0=MERGIN
            y1=HEIGHT-MERGIN
            self.canvas1.create_line(x0,y0,x1,y1,width=lwidth,fill=color)
            x0=MERGIN
            x1=WIDTH-MERGIN
            y0=MERGIN+i*SIDE
            y1=MERGIN+i*SIDE
            self.canvas1.create_line(x0,y0,x1,y1,width=lwidth,fill=color)
            self.canvas1.bind('<Button-1>',self.__cell_click)
    ############### For click event#############
    def __cell_click(self,event):
        x,y=event.x,event.y
        if (MERGIN<x<WIDTH-MERGIN and MERGIN<y<HEIGHT-MERGIN):
            self.canvas1.focus_set()
            self.row,self.col=(y-MERGIN)//SIDE, (x-MERGIN)//SIDE
            self.__createREC()
            self.canvas1.bind('<Key>',self.__write)
    ################### For Show click Area #############
    def __createREC(self):
        x0=self.col*SIDE+MERGIN
        y0=self.row*SIDE+MERGIN
        x1,y1=x0+SIDE, y0+SIDE
        self.canvas1.delete('rec')
        self.canvas1.create_rectangle(x0,y0,x1,y1,width=2,outline='red',tag='rec')

    ############## For adding user input to main window###############
    def __write(self,event):
        if event.keysym=='Return':          #press Enter key
            self.__solve()
        elif event.keysym=='BackSpace':
            self.canvas1.delete(self.num[self.row][self.col])
            self.canvas1.update()
            self.mainarr[self.row][self.col]=0
            self.count=True
            self.__clarr[self.row][self.col]=0
        elif event.keysym=='Up':
            if self.row>0:
                self.row-=1
                self.__createREC()
        elif event.keysym=='Down':
            if self.row<8: 
                self.row+=1
                self.__createREC()
        elif event.keysym=='Left':
            if self.col>0:
                self.col-=1
                self.__createREC()
            else:
                if self.row>0:
                    self.row-=1
                    self.col=8
                    self.__createREC()
        elif event.keysym=='Right':
            if self.col<8:
                self.col+=1
                self.__createREC()
            else:
                if self.row<8:
                    self.row+=1
                    self.col=0
                    self.__createREC()
        elif event.keysym=='Shift_R':
            pass
        elif event.char in '123456789':
            x=self.col*SIDE+MERGIN+SIDE/2
            y=self.row*SIDE+MERGIN+SIDE/2
            self.canvas1.delete(self.num[self.row][self.col])
            self.num[self.row][self.col]=self.canvas1.create_text(x,y,text=int(event.char),font=40,fill='blue',tag='char')
            if self.possible(self.col,self.row,int(event.char)):
                self.mainarr[self.row][self.col]=int(event.char)
                self.__clarr[self.row][self.col]=int(event.char)
            else: 
                messagebox.showinfo("Error","You should put valid number")
                time.sleep(0.1)
                self.canvas1.delete(self.num[self.row][self.col])
                if self.mainarr[self.row][self.col]!=0:
                    self.num[self.row][self.col]=self.canvas1.create_text(x,y,text=self.mainarr[self.row][self.col],fill='blue',font=40,tag='char')
    ######################## Printing the result after solving################       
    def __printing(self):
        self.canvas1.delete('char')
        self.canvas1.delete('rec')
        for i in range(9):
            for j in range(9):
                #print(self.__clarr)
                col='blue' if self.__clarr[i][j]==self.mainarr[i][j] else 'black'
                x=j*SIDE+MERGIN+SIDE/2
                y=i*SIDE+MERGIN+SIDE/2
                self.num[i][j]=self.canvas1.create_text(x,y,text=self.mainarr[i][j],font=40,fill=col,tag='char')
                self.canvas1.update()
    ################################ Backtrack  ###################################
    ################### Testing user input, and testing num is valid while solving####
    def possible(self,x, y, n):
        for i in range(0, 9):
            if self.mainarr[i][x] == n and i != y: # Checks for number (n) in X columns
                return False

        for i in range(0, 9):
            if self.mainarr[y][i] == n and i != x: # Checks for number (n) in X columns
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for X in range(x0, x0 + 3):
            for Y in range(y0, y0 + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
                if self.mainarr[Y][X] == n:
                    return False    
        return True
    ########### solving with backtracking algorithm############
    def __solve(self):
        while True:
            for y in range(9):
                for x in range(9):
                    if self.mainarr[y][x] == 0:
                        for n in range(1, 10):
                            if self.possible(x, y, n):
                                self.mainarr[y][x] = n
                                if self.count==True:
                                    self.__solve()
                                    if self.count==True:
                                        self.mainarr[y][x] = 0
                        return
            if self.count==True:
                self.__printing()
            self.count=False
            return False
    ############################################################################################
    ################ clear the screen and clear main array ##############
    def __clearalltext(self):
        self.canvas1.delete('char')
        self.canvas1.update()
        self.mainarr=[[0]*9 for i in [0]*9]
        self.canvas1.delete('rec')
        self.__clarr=[[0]*9 for i in [0]*9]
        self.count=True
    #########run this program in mainloop ############
    def run(self):
        self.window.mainloop()
#####################################################################
##### To escape from calling another namespace ##################
if __name__ == "__main__":
    mysudoku=sudoku()
    mysudoku.run()