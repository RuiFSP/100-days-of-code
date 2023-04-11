import tkinter as tk

from typingtestgui import TypingTestGUI


class TypingTestApp:
    """
    The main application class that creates the GUI and runs the event loop.
    """

    def __init__(self, test_string):
        """
        Creates a new TypingTestApp instance.

        Parameters
        ----------
        test_string : str
            The text that the user needs to type.
        """
        self.root = tk.Tk()
        self.typing_test_gui = TypingTestGUI(self.root, test_string)

    def run(self):
        """
        Runs the application event loop.
        """
        self.root.mainloop()
