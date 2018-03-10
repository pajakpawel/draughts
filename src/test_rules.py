from unittest import TestCase
from layout import Window
from logic import Rules, Tk
from draughtsmen import Draughtsmen
from unittest.mock import patch


class TestRules(TestCase):
    def test_changeTurn(self):

        root = Tk()
        window = Window(root)

        Draughtsmen.canCapture_C = True
        Draughtsmen.canCapture_B = True
        window.turnText.set('Ruch B')

        with patch.object(Rules,'endGame') as endGame_call:
            with patch.object(Rules, 'createDames') as createDames_call:
                Rules.changeTurn(window.turnText)

                endGame_call.assert_called_with(window.turnText)
                createDames_call.assert_called_with(window.turnText)

        self.assertFalse(Draughtsmen.canCapture_C)
        self.assertFalse(Draughtsmen.canCapture_B)
        self.assertEqual('Ruch C',window.turnText.get())
