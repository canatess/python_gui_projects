# Import Libraries.
from PyQt5 import QtCore, QtWidgets


# Class to Design App Window.
class AppWindow(object):

    # Initialize App Window Design.
    def __init__(self, main_window):

        # Customize Window Settings.
        main_window.setObjectName("MainWindow")
        main_window.resize(664, 520)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.image = QtWidgets.QLabel(self.central_widget)
        self.image.setGeometry(QtCore.QRect(20, 10, 631, 351))
        self.image.setText("")
        self.image.setObjectName("image")

        # Customize Selection Buttons.
        self.mcqueen = QtWidgets.QPushButton(self.central_widget)
        self.mcqueen.setGeometry(QtCore.QRect(20, 380, 301, 91))
        self.mcqueen.setObjectName("mcqueen")

        self.optimus = QtWidgets.QPushButton(self.central_widget)
        self.optimus.setGeometry(QtCore.QRect(350, 380, 291, 91))
        self.optimus.setObjectName("pushButton_2")

        # Customize Window Settings with Buttons.
        main_window.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 18))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        # Set Text to Objects.
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Image Selector"))
        self.mcqueen.setText(_translate("MainWindow", "McQueen"))
        self.optimus.setText(_translate("MainWindow", "Optimus Prime"))

        # Create Connection Between Objects and Names.
        QtCore.QMetaObject.connectSlotsByName(main_window)
