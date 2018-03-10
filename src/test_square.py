from unittest import TestCase
from unittest.mock import patch
from layout import Window
from buttons import *


class TestSquare(TestCase):
    def test_move(self):

        root = Tk()
        window = Window(root)

        square = Square(root, window.turnText, coordinate_i=4, coordinate_j=3,
                        draughtsmen=Draughtsmen(window.turnText, player='B',coordinate_i=4,coordinate_j=3))

        self.assertRaises(NiedozwolonyRuch, square.move)

        square.draughtsmen = None
        Draughtsmen.previousCoordinate_j = 4
        Draughtsmen.previousCoordinate_i = 5
        Draughtsmen.prevoiusMarked = '[B]'

        with patch.object(Square, 'swap') as swap_call:
            with patch.object(Rules, 'changeTurn') as changeTurn_call:
                square.move()

                swap_call.assert_called_with()
                changeTurn_call.assert_called_with(square.turnText)
