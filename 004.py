# Combo Box & Label
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QCheckBox, QRadioButton, QHBoxLayout, QComboBox
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
        self.url = requests.get(
            "https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json")
        self.response = self.url.json()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label.addLabel("Product 004.py"))
        category = list(set(map(lambda a: a['category'], self.response)))
        for cr in category:
            cate = self.layout.addWidget(QLabel(cr))
            var = cr
            combo = QComboBox()
            self.layout.addWidget(combo)

            for i in range(len(self.response)):
                if var == self.response[i]['category']:
                    combo.addItem(self.response[i]['name'])

        self.layout.addWidget(combo)

    def setWidget(self):
        # object widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        # set "object widget" to centralWidget of mainWindow()
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
    window.setWindowTitle("004.py")
    window.show()
    app.exec_()
