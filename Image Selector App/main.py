"""
@Project_Description:
    Change image with buttons.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from AppDesign.design import AppWindow


# Class to Run App.
class App(QtWidgets.QMainWindow):

    # Initialize App.
    def __init__(self):
        super(App, self).__init__()
        self.UI = AppWindow(self)
        self.UI.mcqueen.clicked.connect(self.load_mcqueen)
        self.UI.optimus.clicked.connect(self.load_optimus)
        self.show()

    # Load McQueen Image.
    def load_mcqueen(self):
        self.pixmap = QPixmap("Media/McQueen.jpg")
        self.UI.image.setPixmap(self.pixmap)

    # Load Optimus Prime Image.
    def load_optimus(self):
        self.pixmap = QPixmap("Media/Optimus.jpg")
        self.UI.image.setPixmap(self.pixmap)


# Run Program.
if __name__ == "__main__":
    app_widget = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(app_widget.exec())
