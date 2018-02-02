from draughtsmen import *


class Rules:

    @staticmethod
    def changeTurn(turnText):
        Draughtsmen.canCapture_B = False
        Draughtsmen.canCapture_C = False

        if turnText.get() == 'Ruch B':
            turnText.set('Ruch C')
        else:
            turnText.set('Ruch B')

        Rules.endGame(turnText)
        Rules.createDames(turnText)

    @staticmethod
    def endGame(turnText):
        anyDraughtsmen_C = False
        anyDraughtsmen_B = False
        anyMove = False

        for tab in layout.Window.chessboard:
            for draughtsmen in tab:
                if (draughtsmen.text.get() == "C" or draughtsmen.text.get() == "Cd"):
                    anyDraughtsmen_C = True
                    break

        for tab in layout.Window.chessboard:
            for draughtsmen in tab:
                if (draughtsmen.text.get() == "B" or draughtsmen.text.get() == "Bd"):
                    anyDraughtsmen_B = True
                    break

        if (turnText.get() == 'Ruch B'):
            for tab in layout.Window.chessboard:
                for draughtsmen in tab:
                    if ((draughtsmen.text.get() == "B" or draughtsmen.text.get() == "Bd") and draughtsmen.coordinate_i > 0):
                        draughtsmen.canCapture()
                        if (draughtsmen.coordinate_j > 0):
                            left_jump = layout.Window.chessboard[draughtsmen.coordinate_i - 1][draughtsmen.coordinate_j - 1]

                            if (left_jump.draughtsmen == None):
                                anyMove = True
                                break
                        if (draughtsmen.coordinate_j < 7):
                            right_jump = layout.Window.chessboard[draughtsmen.coordinate_i - 1][draughtsmen.coordinate_j + 1]

                            if (right_jump.draughtsmen == None):
                                anyMove = True
                                break

                    if (draughtsmen.text.get() == "Bd" and draughtsmen.coordinate_i < 7):
                        draughtsmen.canCapture()
                        if (draughtsmen.coordinate_j > 0):
                            left_jump = layout.Window.chessboard[draughtsmen.coordinate_i + 1][draughtsmen.coordinate_j - 1]

                            if (left_jump.draughtsmen == None):
                                anyMove = True
                                break

                        if (draughtsmen.coordinate_j < 7):
                            right_jump = layout.Window.chessboard[draughtsmen.coordinate_i + 1][draughtsmen.coordinate_j + 1]

                            if (right_jump.draughtsmen == None):
                                anyMove = True
                                break
        else:
            for tab in layout.Window.chessboard:
                for draughtsmen in tab:
                    if ((draughtsmen.text.get() == "C" or draughtsmen.text.get() == "Cd") and draughtsmen.coordinate_i < 7):
                        draughtsmen.canCapture()
                        if (draughtsmen.coordinate_j > 0):
                            left_jump = layout.Window.chessboard[draughtsmen.coordinate_i + 1][draughtsmen.coordinate_j - 1]

                            if (left_jump.draughtsmen == None):
                                anyMove = True
                                break

                        if (draughtsmen.coordinate_j < 7):
                            right_jump = layout.Window.chessboard[draughtsmen.coordinate_i + 1][draughtsmen.coordinate_j + 1]

                            if (right_jump.draughtsmen == None):
                                anyMove = True
                                break

                    if (draughtsmen.text.get() == "Cd" and draughtsmen.coordinate_i > 0):
                        draughtsmen.canCapture()
                        if (draughtsmen.coordinate_j > 0):
                            left_jump = layout.Window.chessboard[draughtsmen.coordinate_i - 1][draughtsmen.coordinate_j - 1]

                            if (left_jump.draughtsmen == None):
                                anyMove = True
                                break

                        if (draughtsmen.coordinate_j < 7):
                            right_jump = layout.Window.chessboard[draughtsmen.coordinate_i - 1][draughtsmen.coordinate_j + 1]

                            if (right_jump.draughtsmen == None):
                                anyMove = True
                                break

        if (not anyDraughtsmen_C) or (turnText.get() == 'Ruch C' and anyMove == False and Draughtsmen.canCapture_C == False):
            messagebox.showinfo("Koniec gry ", "Wygral gracz B :D")

        elif (not anyDraughtsmen_B) or (turnText.get() == 'Ruch B' and anyMove == False and Draughtsmen.canCapture_B == False):
            messagebox.showinfo("Koniec gry ", "Wygral gracz C :D")

        Draughtsmen.canCapture_B = False
        Draughtsmen.canCapture_C = False

    @staticmethod
    def createDames(turnText):
        for j in range(8):
            if layout.Window.chessboard[0][j].text.get()=='B':
                layout.Window.chessboard[0][j].draughtsmen = Dame(turnText, 'Bd', 0, j)
                layout.Window.chessboard[0][j].text.set('Bd')

        for j in range(8):
            if layout.Window.chessboard[7][j].text.get() == 'C':
                layout.Window.chessboard[7][j].draughtsmen = Dame(turnText, 'Cd', 7, j)
                layout.Window.chessboard[7][j].text.set('Cd')