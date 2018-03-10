from tkinter import *
from tkinter import messagebox
import layout

class Draughtsmen:
    anotherPushed = False
    previousCoordinate_i = 0
    previousCoordinate_j = 0
    prevoiusMarked=""
    canCapture_B = False
    canCapture_C = False

    def __init__(self,turnText,  player='', coordinate_i=0, coordinate_j=0):

        self.turnText = turnText

        self.player=StringVar()
        self.player.set(player)

        self.coordinate_i = coordinate_i
        self.coordinate_j = coordinate_j

    def action(self):
        for i in range(len(layout.Window.chessboard)):
            for j in range(len(layout.Window.chessboard[i])):
                layout.Window.chessboard[i][j].canCapture()

        if (Draughtsmen.anotherPushed == False):

            if (self.player.get() == "B"):
                if (self.turnText.get() == 'Ruch B'):
                    self.player.set("[B]")
                    Draughtsmen.anotherPushed = True
                    Draughtsmen.previousCoordinate_i = self.coordinate_i
                    Draughtsmen.previousCoordinate_j = self.coordinate_j
                    Draughtsmen.prevoiusMarked = "[B]"
            elif (self.player.get() == "C"):
                if (self.turnText.get() == 'Ruch C'):
                    self.player.set("[C]")
                    Draughtsmen.anotherPushed = True
                    Draughtsmen.previousCoordinate_i = self.coordinate_i
                    Draughtsmen.previousCoordinate_j = self.coordinate_j
                    Draughtsmen.prevoiusMarked = "[C]"


        elif (Draughtsmen.anotherPushed == True):
            if (Draughtsmen.previousCoordinate_i == self.coordinate_i and Draughtsmen.previousCoordinate_j == self.coordinate_j):
                if (self.player.get() == "[B]"):
                    self.player.set("B")
                    Draughtsmen.anotherPushed = False
                    Draughtsmen.previousCoordinate_i = 0
                    Draughtsmen.previousCoordinate_j = 0

                elif (self.player.get() == "[C]"):
                    self.player.set("C")
                    Draughtsmen.anotherPushed = False
                    Draughtsmen.previousCoordinate_i = 0
                    Draughtsmen.previousCoordinate_j = 0
            else:
                messagebox.showerror("ERROR!!", "Ten ruch jest niedozwolony!!!")
        else:
            messagebox.showerror("ERROR!!", "Ten ruch jest niedozwolony!!!")

    def canCapture(self):
        
        if ((self.player.get() == "B" or self.player.get() == "Bd") and self.coordinate_i>1):
            if(self.coordinate_j > 1):
                left_captured = layout.Window.chessboard[self.coordinate_i-1][self.coordinate_j-1]
                left_jump = layout.Window.chessboard[self.coordinate_i-2][self.coordinate_j-2]
                if((left_captured.text.get() == "C" or left_captured.text.get() == "Cd")  and left_jump.draughtsmen == None):
                    Draughtsmen.canCapture_B = True
            if(self.coordinate_j < 6):
                right_captured = layout.Window.chessboard[self.coordinate_i-1][self.coordinate_j+1]
                right_jump = layout.Window.chessboard[self.coordinate_i-2][self.coordinate_j+2]
                if((right_captured.text.get() == "C" or right_captured.text.get() == "Cd") and right_jump.draughtsmen == None):
                    Draughtsmen.canCapture_B = True


        elif((self.player.get() == "C" or self.player.get() == "Cd") and self.coordinate_i < 6):
            if(self.coordinate_j > 1):
                left_captured = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1]
                left_jump = layout.Window.chessboard[self.coordinate_i + 2][self.coordinate_j - 2]
                if ((left_captured.text.get() == "B" or left_captured.text.get()=="Bd") and left_jump.draughtsmen == None):
                    Draughtsmen.canCapture_C = True

            if(self.coordinate_j<6):
                right_captured = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1]
                right_jump = layout.Window.chessboard[self.coordinate_i + 2][self.coordinate_j + 2]
                if ((right_captured.text.get() == "B"  or right_captured.text.get()=="Bd") and right_jump.draughtsmen == None):
                    Draughtsmen.canCapture_C = True


class Dame(Draughtsmen):

    def __init__(self, turnText,  player='', coordinate_i=0, coordinate_j=0):
        super().__init__(turnText,  player, coordinate_i, coordinate_j)

    def action(self):
        for i in range(len(layout.Window.chessboard)):
            for j in range(len(layout.Window.chessboard[i])):
                layout.Window.chessboard[i][j].canCapture()

        if (Draughtsmen.anotherPushed == False):

            if (self.player.get() == "Bd"):
                if (self.turnText.get() == 'Ruch B'):
                    self.player.set("[Bd]")
                    Draughtsmen.anotherPushed = True
                    Draughtsmen.previousCoordinate_i = self.coordinate_i
                    Draughtsmen.previousCoordinate_j = self.coordinate_j
                    Draughtsmen.prevoiusMarked = "[Bd]"

            elif (self.player.get() == "Cd"):
                if (self.turnText.get() == 'Ruch C'):
                    self.player.set("[Cd]")
                    Draughtsmen.anotherPushed = True
                    Draughtsmen.previousCoordinate_i = self.coordinate_i
                    Draughtsmen.previousCoordinate_j = self.coordinate_j
                    Draughtsmen.prevoiusMarked = "[Cd]"
        elif (Draughtsmen.anotherPushed == True):
            if (Draughtsmen.previousCoordinate_i == self.coordinate_i and Draughtsmen.previousCoordinate_j == self.coordinate_j):
                if (self.player.get() == "[Bd]"):
                    self.player.set("Bd")
                    Draughtsmen.anotherPushed = False
                    Draughtsmen.previousCoordinate_i = 0
                    Draughtsmen.previousCoordinate_j = 0

                elif (self.player.get() == "[Cd]"):
                    self.player.set("Cd")
                    Draughtsmen.anotherPushed = False
                    Draughtsmen.previousCoordinate_i = 0
                    Draughtsmen.previousCoordinate_j = 0
            else:
                messagebox.showerror("ERROR!!", "Ten ruch jest niedozwolony!!!")
        else:
            messagebox.showerror("ERROR!!", "Ten ruch jest niedozwolony!!!")

            

    def canCapture(self):
        super().canCapture()

        if (self.player.get() == "Bd" and self.coordinate_i < 6):
            if (self.coordinate_j > 1):
                left_captured = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1]
                left_jump = layout.Window.chessboard[self.coordinate_i + 2][self.coordinate_j - 2]
                if ((left_captured.text.get() == "C" or left_captured.text.get() == "Cd") and left_jump.draughtsmen == None):
                    Draughtsmen.canCapture_B = True

            if (self.coordinate_j < 6):
                right_captured = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1]
                right_jump = layout.Window.chessboard[self.coordinate_i + 2][self.coordinate_j + 2]
                if ((right_captured.text.get() == "C" or right_captured.text.get() == "Cd") and right_jump.draughtsmen == None):
                    Draughtsmen.canCapture_B = True

        elif (self.player.get() == "Cd" and self.coordinate_i > 1):
            if (self.coordinate_j > 1):
                left_captured = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1]
                left_jump = layout.Window.chessboard[self.coordinate_i - 2][self.coordinate_j - 2]
                if ((left_captured.text.get() == "B" or left_captured.text.get() == "Bd") and left_jump.draughtsmen == None):
                    Draughtsmen.canCapture_C = True

            if (self.coordinate_j < 6):
                right_captured = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1]
                right_jump = layout.Window.chessboard[self.coordinate_i - 2][self.coordinate_j + 2]
                if ((right_captured.text.get() == "B" or right_captured.text.get() == "Bd") and right_jump.draughtsmen == None):
                    Draughtsmen.canCapture_C = True
