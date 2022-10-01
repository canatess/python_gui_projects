"""
@Project_Description:
    Convert money currencies in real time with using an API.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import sys
import requests
from PyQt5 import QtWidgets
from AppDesign.design import AppWindow


# Class to Run App.
class App(QtWidgets.QMainWindow):

    # Initialize App.
    def __init__(self):
        super(App, self).__init__()
        self.UI = AppWindow(self)
        self.UI.AUD.clicked.connect(lambda: self.convert(self.UI.AUD.text()))
        self.UI.BRL.clicked.connect(lambda: self.convert(self.UI.BRL.text()))
        self.UI.CAD.clicked.connect(lambda: self.convert(self.UI.CAD.text()))
        self.UI.CHF.clicked.connect(lambda: self.convert(self.UI.CHF.text()))
        self.UI.CNY.clicked.connect(lambda: self.convert(self.UI.CNY.text()))
        self.UI.EUR.clicked.connect(lambda: self.convert(self.UI.EUR.text()))
        self.UI.GBP.clicked.connect(lambda: self.convert(self.UI.GBP.text()))
        self.UI.HKD.clicked.connect(lambda: self.convert(self.UI.HKD.text()))
        self.UI.INR.clicked.connect(lambda: self.convert(self.UI.INR.text()))
        self.UI.JPY.clicked.connect(lambda: self.convert(self.UI.JPY.text()))
        self.UI.KRW.clicked.connect(lambda: self.convert(self.UI.KRW.text()))
        self.UI.MXN.clicked.connect(lambda: self.convert(self.UI.MXN.text()))
        self.UI.NOK.clicked.connect(lambda: self.convert(self.UI.NOK.text()))
        self.UI.NZD.clicked.connect(lambda: self.convert(self.UI.NZD.text()))
        self.UI.RUB.clicked.connect(lambda: self.convert(self.UI.RUB.text()))
        self.UI.SEK.clicked.connect(lambda: self.convert(self.UI.SEK.text()))
        self.UI.SGD.clicked.connect(lambda: self.convert(self.UI.SGD.text()))
        self.UI.TRY.clicked.connect(lambda: self.convert(self.UI.TRY.text()))
        self.UI.USD.clicked.connect(lambda: self.convert(self.UI.USD.text()))
        self.UI.ZAR.clicked.connect(lambda: self.convert(self.UI.ZAR.text()))

    # Convert Currencies with Using a Currency Exchanger API.
    def convert(self, currency):
        base_currency = self.UI.currency_input.text()
        money_amount = float(self.UI.amount_input.text())

        parameters = {'base': base_currency.upper(),
                      'amount': money_amount,
                      'symbols': currency}

        response = requests.get(url='https://api.exchangerate.host/latest', params=parameters)
        data = response.json()['rates']

        result = ""
        for item in data.items():
            result += f"{money_amount} {base_currency.upper()} = {item[1]:.2f} {item[0]}" + "\n"

        self.UI.result_label.setText(result)


# Run Program.
if __name__ == "__main__":
    app_widget = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(app_widget.exec_())
