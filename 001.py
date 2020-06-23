from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QVBoxLayout, QWidget
import random


class GenerateApp(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GenerateApp, self).__init__(*args, **kwargs)
        self.label = Labiles()
        self.mainWidget()
        self.setLayout()
        self.setWidget()

    def mainWidget(self):
        # combo box
        self.comboBox = QComboBox()
        self.comboBox.addItem("orange")
        self.comboBox.addItem("apple")
        self.comboBox.addItem("mango")
        self.comboBox.addItem("grape")
        self.comboBox.addItem("peach")
        self.comboBox.addItem("watermelon")

    def setLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label.addLabelis("datalist"))
        self.layout.addWidget(self.comboBox)

    def setWidget(self):
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


class Labiles():
    def addLabelis(self, text):
        self.label = QLabel(text)
        return self.label


if __name__ == "__main__":
    app = QApplication([])
    generates = GenerateApp()
    generates.show()
    app.exec_()
