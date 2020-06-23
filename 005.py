# Check Box
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt


class CheckBoxApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CheckBoxApp, self).__init__(*args, **kwargs)
        self.label = Labels()
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        pass

    def setLayout(self):
        self.url = requests.get("https://randomuser.me/api/?results=10")
        self.url = self.url.json()
        self.response = self.url['results']
        self.results = list(map(lambda x: "{} {} {}".format(
            x['name']['title'], x['name']['first'], x['name']['last']), self.response))

        zero = 0
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label.addLabel("Title,First,Last"))
        for x in self.results:
            zero += 1
            self.finish = "check_{}".format(zero)
            self.finish = QCheckBox(x)
            self.layout.addWidget(self.finish)

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
    window = CheckBoxApp()
    window.setWindowTitle("005.py")
    window.show()
    app.exec_()
