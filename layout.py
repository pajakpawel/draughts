from buttons import *

class Window:

    chessboard = [[] for i in range(8)]

    def __init__(self,root):

        self.root = root

        self.turnText = StringVar()

        self.letterList = []
        self.numberList = []

        self.describeWindow(self.root)
        self.defaultLayout(self.root)

    def describeWindow(self,root):
        px = 1
        py = 5

        self.turnText.set('')
        self.turn = Label(root, textvariable=self.turnText)
        self.turn.grid(row=2, column=5, sticky=E)

        # UPPER LETTERS
        column = 2
        for letter in range (65,73):
            self.letterList.append(Label(root, text=chr(letter)))
            self.letterList[-1].grid(row=5, column=column, sticky=N, padx=px, pady=py)
            column += 1

        # LEFT DIGITS
        row = 6
        for number in range(8,0,-1):
            self.numberList.append(Label(root, text=number))
            self.numberList[-1].grid(row=row, column=1, padx=px, pady=py)
            row += 1


        #RIGHT BUTTONS
        self.reset_button = Button(root, activebackground="MediumOrchid1", background="MediumOrchid1", command=lambda: self.resetWindow(root),
                             text="Reset planszy", width=15, height=3)
        self.reset_button.grid(row=6, column=10, padx=20, pady=0)

        self.test_button = Button(root, activebackground="MediumOrchid1", background="MediumOrchid1", command=lambda: self.testLayout(root),
                                   text="TESTY", width=15, height=3)
        self.test_button.grid(row=7, column=10, padx=20, pady=0)

    def resetWindow(self,root):
        for widget in root.winfo_children():
            widget.destroy()

        Window.chessboard = [[] for i in range(8)]
        self.describeWindow(root)
        self.defaultLayout(root)
        Draughtsmen.canCapture_B = False
        Draughtsmen.canCapture_C = False
        Draughtsmen.anotherPushed = False

    def testLayout(self,root):
        for widget in root.winfo_children():
            widget.destroy()

        Window.chessboard = [[] for i in range(8)]
        self.describeWindow(root)
        self.turnText.set('Ruch B')

        for i in range(8):

            row = i + 6
            column = 2
            if (i < 3):
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                           Window.chessboard[i].append(Square(root, self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(PushButton(root, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2,
                                                             draughtsmen=Draughtsmen( self.turnText, player='C', coordinate_i=i,
                                                                                     coordinate_j=column - 2)))
                        column += 1
            elif (i < 5):
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                           Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
            else:
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2,
                                                             draughtsmen=Draughtsmen( self.turnText, player='B', coordinate_i=i,
                                                                                     coordinate_j=column - 2)))
                        else:
                            Window.chessboard[i].append(PushButton(root, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1

        Draughtsmen.canCapture_B = False
        Draughtsmen.canCapture_C = False
        Draughtsmen.anotherPushed = False

    def defaultLayout(self,root):
        self.turnText.set('Ruch B')

        for i in range(8):

            row = i + 6
            column = 2
            if (i < 3):
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(Square(root,self.turnText,row = row,column = column,coordinate_i = i, coordinate_j = column - 2,
                                                             draughtsmen = Draughtsmen(self.turnText,player='C',coordinate_i = i, coordinate_j = column - 2)))
                        else:
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2,
                                                             draughtsmen=Draughtsmen( self.turnText, player='C', coordinate_i=i,
                                                                                     coordinate_j=column - 2)))
                        column += 1
            elif (i < 5):
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
            else:
                if (not i % 2):

                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2,
                                                             draughtsmen=Draughtsmen( self.turnText, player='B', coordinate_i=i,
                                                                                     coordinate_j=column - 2)))
                        else:
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        column += 1
                else:
                    while (column <= 9):
                        if (column % 2):
                            Window.chessboard[i].append(PushButton(root,  row=row, column=column, coordinate_i=i, coordinate_j=column - 2))
                        else:
                            Window.chessboard[i].append(Square(root,  self.turnText, row=row, column=column, coordinate_i=i, coordinate_j=column - 2,
                                                             draughtsmen=Draughtsmen( self.turnText, player='B', coordinate_i=i,
                                                                                     coordinate_j=column - 2)))
                        column += 1