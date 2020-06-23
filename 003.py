## from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt
import requests


class JsonPlace(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(JsonPlace, self).__init__(*args, **kwargs)
        self.label = Labels()
        self.setLayout()
        self.setWidget()

    def setLayout(self):
        # object layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label.addLabel("name and data Json"))
        url = requests.get('https://randomuser.me/api/?results=10')
        response = url.json()
        for x in response:
            self.layout.addWidget(self.label.addLabel('Gender: {}'.format(
                x['gender'])))

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        # set "object widget" to centralWidget of mainWindow()
        # centralWidget() hanya menerima satu widget
        self.setCentralWidget(self.widget)


class checkBoxs():
    def __init__(self, text):
        self.addCheckBox = QCheckBox(text)


class Labels():
    def addLabel(self, text):
        self.label = QLabel(text)
        return self.label


if __name__ == "__main__":
    app = QApplication([])
    window = JsonPlace()
    window.show()
    app.exec_()
