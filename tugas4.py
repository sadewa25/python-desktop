# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:51:40 2022

@author: Hanson
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtGui import QFont

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Score Grading")
        self.setFixedSize(QSize(300, 200))

        self.label = QLabel()
        self.label.setFont(QFont('Arial', 15))

        self.input = QLineEdit()
        self.input.textChanged.connect(self.onTextChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def onTextChanged(self, text):
        score = int(text)
        if (score >= 90 and score <= 100):
            self.label.setText('A')
        elif (score >= 70 and score <= 89):
            self.label.setText('B')
        elif (score >= 50 and score <= 69):
            self.label.setText('C')
        elif (score >= 0 and score <= 49):
            self.label.setText('D')
        else:
            self.label.clear()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()