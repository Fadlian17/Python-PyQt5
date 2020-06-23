# Combo Box Filter Data

import sys
import random
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def Filter():
    app = QApplication(sys.argv)
    widget = QWidget()
    comboBox = QComboBox(widget)
    http = requests.get('https://randomuser.me/api/?results=10')
    http_response = http.json()['results']
    http_response = [http_response[i]['gender']
                     for i in range(len(http_response))]
    http_response = list(set(http_response))
    # loop
    for hr in http_response:
        comboBox.addItem(hr)

    widget.setFixedSize(200, 200)
    widget.setWindowTitle("003.py")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Filter()
