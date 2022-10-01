# Import Libraries.
from PyQt5 import QtCore, QtGui, QtWidgets


# Class to Design App Window.
class AppWindow(object):

    # Initialize App Window Design.
    def __init__(self, main_window):

        # Customize Font Settings.
        font = QtGui.QFont()
        font.setPointSize(14)

        # Customize Window Settings.
        main_window.setObjectName("MainWindow")
        main_window.resize(741, 529)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        main_window.setCentralWidget(self.central_widget)

        self.currency_input = QtWidgets.QLineEdit(self.central_widget)
        self.currency_input.setGeometry(QtCore.QRect(270, 70, 421, 41))
        self.currency_input.setObjectName("currency_input")

        self.amount_input = QtWidgets.QLineEdit(self.central_widget)
        self.amount_input.setGeometry(QtCore.QRect(270, 20, 421, 41))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.amount_input.sizePolicy().hasHeightForWidth())
        self.amount_input.setSizePolicy(size_policy)
        self.amount_input.setObjectName("amount_input")

        self.money_amount = QtWidgets.QLabel(self.central_widget)
        self.money_amount.setGeometry(QtCore.QRect(60, 20, 211, 41))
        self.money_amount.setFont(font)
        self.money_amount.setObjectName("money_amount")

        self.base_currency = QtWidgets.QLabel(self.central_widget)
        self.base_currency.setGeometry(QtCore.QRect(60, 70, 211, 41))
        self.base_currency.setFont(font)
        self.base_currency.setObjectName("base_currency")

        self.result_label = QtWidgets.QLabel(self.central_widget)
        self.result_label.setGeometry(QtCore.QRect(50, 410, 641, 51))
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 140, 641, 231))
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("grid_layout")

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 741, 18))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        # Customize Currency Buttons.
        self.AUD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.AUD.setFont(font)
        self.AUD.setObjectName("AUD")
        self.grid_layout.addWidget(self.AUD, 0, 0, 1, 1)

        self.TRY = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.TRY.setFont(font)
        self.TRY.setObjectName("TRY")
        self.grid_layout.addWidget(self.TRY, 4, 1, 1, 1)

        self.BRL = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.BRL.setFont(font)
        self.BRL.setObjectName("BRL")
        self.grid_layout.addWidget(self.BRL, 0, 1, 1, 1)

        self.CAD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CAD.setFont(font)
        self.CAD.setObjectName("CAD")
        self.grid_layout.addWidget(self.CAD, 0, 2, 1, 1)

        self.JPY = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.JPY.setFont(font)
        self.JPY.setObjectName("JPY")
        self.grid_layout.addWidget(self.JPY, 2, 1, 1, 1)

        self.EUR = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.EUR.setFont(font)
        self.EUR.setObjectName("EUR")
        self.grid_layout.addWidget(self.EUR, 1, 1, 1, 1)

        self.SGD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SGD.setFont(font)
        self.SGD.setObjectName("SGD")
        self.grid_layout.addWidget(self.SGD, 4, 0, 1, 1)

        self.INR = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.INR.setFont(font)
        self.INR.setObjectName("INR")
        self.grid_layout.addWidget(self.INR, 2, 0, 1, 1)

        self.CNY = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CNY.setFont(font)
        self.CNY.setObjectName("CNY")
        self.grid_layout.addWidget(self.CNY, 1, 0, 1, 1)

        self.NZD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NZD.setFont(font)
        self.NZD.setObjectName("NZD")
        self.grid_layout.addWidget(self.NZD, 3, 1, 1, 1)

        self.NOK = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NOK.setFont(font)
        self.NOK.setObjectName("NOK")
        self.grid_layout.addWidget(self.NOK, 3, 0, 1, 1)

        self.USD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.USD.setFont(font)
        self.USD.setObjectName("USD")
        self.grid_layout.addWidget(self.USD, 4, 2, 1, 1)

        self.GBP = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.GBP.setFont(font)
        self.GBP.setObjectName("GBP")
        self.grid_layout.addWidget(self.GBP, 1, 2, 1, 1)

        self.KRW = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.KRW.setFont(font)
        self.KRW.setObjectName("KRW")
        self.grid_layout.addWidget(self.KRW, 2, 2, 1, 1)

        self.RUB = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.RUB.setFont(font)
        self.RUB.setObjectName("RUB")
        self.grid_layout.addWidget(self.RUB, 3, 2, 1, 1)

        self.CHF = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CHF.setFont(font)
        self.CHF.setObjectName("CHF")
        self.grid_layout.addWidget(self.CHF, 0, 3, 1, 1)

        self.HKD = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.HKD.setFont(font)
        self.HKD.setObjectName("HKD")
        self.grid_layout.addWidget(self.HKD, 1, 3, 1, 1)

        self.MXN = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.MXN.setFont(font)
        self.MXN.setObjectName("MXN")
        self.grid_layout.addWidget(self.MXN, 2, 3, 1, 1)

        self.SEK = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SEK.setFont(font)
        self.SEK.setObjectName("SEK")
        self.grid_layout.addWidget(self.SEK, 3, 3, 1, 1)

        self.ZAR = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ZAR.setFont(font)
        self.ZAR.setObjectName("ZAR")
        self.grid_layout.addWidget(self.ZAR, 4, 3, 1, 1)

        # Set Text to Objects.
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Currency Exchanger"))
        self.money_amount.setText(_translate("MainWindow", "Money Amount:"))
        self.base_currency.setText(_translate("MainWindow", "Base Currency:"))
        self.AUD.setText(_translate("MainWindow", "AUD"))
        self.TRY.setText(_translate("MainWindow", "TRY"))
        self.BRL.setText(_translate("MainWindow", "BRL"))
        self.CAD.setText(_translate("MainWindow", "CAD"))
        self.JPY.setText(_translate("MainWindow", "JPY"))
        self.EUR.setText(_translate("MainWindow", "EUR"))
        self.SGD.setText(_translate("MainWindow", "SGD"))
        self.INR.setText(_translate("MainWindow", "INR"))
        self.CNY.setText(_translate("MainWindow", "CNY"))
        self.NZD.setText(_translate("MainWindow", "NZD"))
        self.NOK.setText(_translate("MainWindow", "NOK"))
        self.USD.setText(_translate("MainWindow", "USD"))
        self.GBP.setText(_translate("MainWindow", "GBP"))
        self.KRW.setText(_translate("MainWindow", "KRW"))
        self.RUB.setText(_translate("MainWindow", "RUB"))
        self.CHF.setText(_translate("MainWindow", "CHF"))
        self.HKD.setText(_translate("MainWindow", "HKD"))
        self.MXN.setText(_translate("MainWindow", "MXN"))
        self.SEK.setText(_translate("MainWindow", "SEK"))
        self.ZAR.setText(_translate("MainWindow", "ZAR"))

        # Create Connection Between Objects and Names.
        QtCore.QMetaObject.connectSlotsByName(main_window)
