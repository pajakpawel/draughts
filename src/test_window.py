from tkinter import Tk
from unittest import TestCase
from unittest.mock import patch
from layout import Window


class TestWindow(TestCase):
    def test_resetButton(self):
        root = Tk()
        window = Window(root)

        with patch.object(Window, 'resetWindow') as resetWindow_call:
            window.reset_button.invoke()

            resetWindow_call.assert_called_with(root)

    def test_testButton(self):
        root = Tk()
        window = Window(root)

        with patch.object(Window, 'testLayout') as testLayout_call:
            window.test_button.invoke()

            testLayout_call.assert_called_with(root)
