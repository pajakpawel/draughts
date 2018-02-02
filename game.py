from layout import *


class Game:

    def __init__(self, root):
        self.window = Window(root)


root=Tk()
game = Game(root)
root.title("Warcaby")
root.resizable(width=False, height=False)
window_width = 700
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_position_horizontal = (screen_width / 2) - (window_width / 2)
window_position_vertical = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, window_position_horizontal, window_position_vertical))
root.mainloop()
