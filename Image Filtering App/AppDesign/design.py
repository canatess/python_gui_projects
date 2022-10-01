# Import Libraries.
from PyQt5 import QtCore, QtGui, QtWidgets


# Class to Design App Window.
class AppWindow(object):

    # Initialize App Window Design.
    def __init__(self, main_window):

        # Customize Font Settings.
        font = QtGui.QFont()
        font.setPointSize(10)

        # Customize Window Settings.
        main_window.setObjectName("MainWindow")
        main_window.resize(970, 558)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.image = QtWidgets.QLabel(self.central_widget)
        self.image.setGeometry(QtCore.QRect(20, 20, 640, 480))
        self.image.setText("")
        self.image.setObjectName("image")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 20, 241, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.effects = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.effects.setContentsMargins(0, 0, 0, 0)
        self.effects.setObjectName("effects")

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 18))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        # Customize App Buttons.
        self.browse_image = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_image.setFont(font)
        self.browse_image.setObjectName("browse_image")
        self.effects.addWidget(self.browse_image)

        self.original_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.original_filter.setFont(font)
        self.original_filter.setObjectName("original_filter")
        self.effects.addWidget(self.original_filter)

        self.gray_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.gray_filter.setFont(font)
        self.gray_filter.setObjectName("gray_filter")
        self.effects.addWidget(self.gray_filter)

        self.bgr_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bgr_filter.setFont(font)
        self.bgr_filter.setObjectName("bgr_filter")
        self.effects.addWidget(self.bgr_filter)

        self.sharper_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sharper_filter.setFont(font)
        self.sharper_filter.setObjectName("sharper_filter")
        self.effects.addWidget(self.sharper_filter)

        self.blur_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.blur_filter.setFont(font)
        self.blur_filter.setObjectName("blur_filter")
        self.effects.addWidget(self.blur_filter)
        main_window.setCentralWidget(self.central_widget)

        # Set Text to Objects.
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Image Filtering App"))
        self.browse_image.setText(_translate("MainWindow", "Browse Image"))
        self.original_filter.setText(_translate("MainWindow", "Original Image"))
        self.gray_filter.setText(_translate("MainWindow", "Activate Gray Filter"))
        self.bgr_filter.setText(_translate("MainWindow", "Activate BGR Filter"))
        self.sharper_filter.setText(_translate("MainWindow", "Activate Sharper Filter"))
        self.blur_filter.setText(_translate("MainWindow", "Activate Blur Filter"))

        # Create Connection Between Objects and Names.
        QtCore.QMetaObject.connectSlotsByName(main_window)
