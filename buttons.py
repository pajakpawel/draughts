from logic import *
import layout

class NiedozwolonyRuch(Exception):
    pass

class Bicie(Exception):
    pass

class PushButton():

    def __init__(self, root, row=0, column=0, color='#0080FF', px=0, py=0, coordinate_i=0, coordinate_j=0):

        self.coordinate_i=coordinate_i
        self.coordinate_j=coordinate_j

        self.root=root

        self.text=StringVar()
        self.text.set('')

        self.button=Button(root, activebackground=color, background=color, command=lambda:self.action(), textvariable=self.text, width=8, height=3)
        self.button.grid(row=row, column=column, padx=px, pady=py)

    def action(self):
        messagebox.showerror("ERROR!!", "To pole planszy jest nieaktywne!")

    def canCapture(self):
        pass


class Square(PushButton):
    def __init__(self, root, turnText, row=0, column=0, color='#00FF00',  px=0, py=0, coordinate_i=0, coordinate_j=0,draughtsmen=None):
        super().__init__(root, row, column, color, px, py, coordinate_i, coordinate_j)

        self.turnText = turnText
        self.draughtsmen = draughtsmen
        if(self.draughtsmen != None):
            self.text.set(self.draughtsmen.player.get())

    def action(self):

        if(self.draughtsmen!=None):
            self.draughtsmen.action()
            self.text.set(self.draughtsmen.player.get())
        else:
            if(Draughtsmen.anotherPushed==True):
                try:
                    if (self.turnText.get() == 'Ruch B' and (Draughtsmen.canCapture_B )):
                        self.capture()
                    elif (self.turnText.get() == 'Ruch C' and (Draughtsmen.canCapture_C )):
                        self.capture()
                    else:
                        self.move()
                except NiedozwolonyRuch as exc:
                    messagebox.showerror("ERROR!!", exc)
                except Bicie as exc:
                    messagebox.showwarning("Warning!", exc)

    def capture(self):
        if (self.draughtsmen == None and (Draughtsmen.prevoiusMarked == "[B]" or Draughtsmen.prevoiusMarked=="[Bd]") and self.coordinate_i + 2 == Draughtsmen.previousCoordinate_i):
            if ( self.coordinate_j == Draughtsmen.previousCoordinate_j - 2 ):
                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j+1]

                if (captured_draughtsmen.text.get() == "C" or captured_draughtsmen.text.get() == "Cd"):

                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_B = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_B):
                        Rules.changeTurn(self.turnText)

            elif (self.coordinate_j == Draughtsmen.previousCoordinate_j + 2):
                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1]

                if (captured_draughtsmen.text.get() == "C" or captured_draughtsmen.text.get() == "Cd"):

                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_B = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_B):
                        Rules.changeTurn(self.turnText)

        elif (self.draughtsmen == None and (Draughtsmen.prevoiusMarked == "[C]" or Draughtsmen.prevoiusMarked == "[Cd]") and self.coordinate_i - 2 == Draughtsmen.previousCoordinate_i):
            if (self.coordinate_j == Draughtsmen.previousCoordinate_j - 2):
                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1]

                if (captured_draughtsmen.text.get() == "B" or captured_draughtsmen.text.get() == "Bd"):

                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_C = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_C ):
                        Rules.changeTurn(self.turnText)

            elif (self.coordinate_j == Draughtsmen.previousCoordinate_j + 2):
                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1]

                if (captured_draughtsmen.text.get() == "B" or captured_draughtsmen.text.get() == "Bd"):
                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_C = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_C):
                        Rules.changeTurn(self.turnText)


        elif (self.draughtsmen == None and Draughtsmen.prevoiusMarked == "[Bd]" and self.coordinate_i - 2 == Draughtsmen.previousCoordinate_i):
            if (self.coordinate_j + 2 == Draughtsmen.previousCoordinate_j):

                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1]

                if (captured_draughtsmen.text.get() == "C" or captured_draughtsmen.text.get() == "Cd"):

                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j + 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_B = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_B):
                        Rules.changeTurn(self.turnText)


            elif (self.coordinate_j - 2 == Draughtsmen.previousCoordinate_j):

                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1]

                if (captured_draughtsmen.text.get() == "C" or captured_draughtsmen.text.get() == "Cd"):

                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i - 1][self.coordinate_j - 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_B = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_B):
                        Rules.changeTurn(self.turnText)

        elif (self.draughtsmen == None and  Draughtsmen.prevoiusMarked == "[Cd]" and self.coordinate_i + 2 == Draughtsmen.previousCoordinate_i):
            if (self.coordinate_j == Draughtsmen.previousCoordinate_j - 2):

                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1]

                if (captured_draughtsmen.text.get() == "B" or captured_draughtsmen.text.get() == "Bd"):

                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j + 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_C = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_C):
                        Rules.changeTurn(self.turnText)

            elif (self.coordinate_j == Draughtsmen.previousCoordinate_j + 2):

                captured_draughtsmen = layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1]

                if (captured_draughtsmen.text.get() == "B" or captured_draughtsmen.text.get() == "Bd"):

                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1].draughtsmen = None
                    layout.Window.chessboard[self.coordinate_i + 1][self.coordinate_j - 1].text.set('')

                    self.swap()
                    Draughtsmen.canCapture_C = False
                    self.canCapture()
                    if (not Draughtsmen.canCapture_C):
                        Rules.changeTurn(self.turnText)

        else:
            raise Bicie("Obowiazuje przymus bicia")

    def move(self):
        if (self.draughtsmen == None and (self.coordinate_j == Draughtsmen.previousCoordinate_j - 1 or self.coordinate_j == Draughtsmen.previousCoordinate_j + 1)):

            if ((Draughtsmen.prevoiusMarked == "[B]" or Draughtsmen.prevoiusMarked == "[Bd]") and self.coordinate_i == Draughtsmen.previousCoordinate_i - 1):
                self.swap()
                Rules.changeTurn(self.turnText)
            elif (Draughtsmen.prevoiusMarked == "[Bd]" and self.coordinate_i == Draughtsmen.previousCoordinate_i + 1):
                self.swap()
                Rules.changeTurn(self.turnText)

            elif ((Draughtsmen.prevoiusMarked == "[C]" or Draughtsmen.prevoiusMarked == "[Cd]") and self.coordinate_i == Draughtsmen.previousCoordinate_i + 1):
                self.swap()
                Rules.changeTurn(self.turnText)
            elif (Draughtsmen.prevoiusMarked == "[Cd]" and self.coordinate_i == Draughtsmen.previousCoordinate_i - 1):
                self.swap()
                Rules.changeTurn(self.turnText)
            else:
                raise NiedozwolonyRuch("Ten ruch jest niedozwolony!!!")

        else:
            raise NiedozwolonyRuch("Ten ruch jest niedozwolony!!")

    def swap(self):

        self.draughtsmen = layout.Window.chessboard[Draughtsmen.previousCoordinate_i][Draughtsmen.previousCoordinate_j].draughtsmen
        self.draughtsmen.coordinate_i = self.coordinate_i
        self.draughtsmen.coordinate_j = self.coordinate_j

        layout.Window.chessboard[Draughtsmen.previousCoordinate_i][Draughtsmen.previousCoordinate_j].draughtsmen = None
        layout.Window.chessboard[Draughtsmen.previousCoordinate_i][Draughtsmen.previousCoordinate_j].text.set('')

        if(self.draughtsmen.player.get() == "[B]"):
            self.draughtsmen.player.set("B")

        elif(self.draughtsmen.player.get() == "[C]"):
            self.draughtsmen.player.set("C")

        elif (self.draughtsmen.player.get() == "[Bd]"):
            self.draughtsmen.player.set("Bd")

        elif (self.draughtsmen.player.get() == "[Cd]"):
            self.draughtsmen.player.set("Cd")

        self.text.set(self.draughtsmen.player.get())

        Draughtsmen.anotherPushed = False
        Draughtsmen.previousCoordinate_i= 0
        Draughtsmen.previousCoordinate_j = 0

    def canCapture(self):
        if(self.draughtsmen != None):
            self.draughtsmen.canCapture()
        else:
            pass
