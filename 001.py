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
        datalist = ["orange", "apple", "mango", "grape", "peach", "watermelon"]
        data_shuffle = random.sample(datalist, len(datalist))
        data_shuffle = self.comboBox.addItems(data_shuffle)
        return self.comboBox

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
    generates.setWindowTitle("001.py")
    generates.show()
    app.exec_()
