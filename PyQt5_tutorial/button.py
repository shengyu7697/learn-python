#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtCore import QCoreApplication

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Button example')
        self.setGeometry(300, 300, 300, 200)

        self.btn = QPushButton('Button', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.onClick)

        btn_quit = QPushButton('Quit', self)
        btn_quit.move(10, 50)
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 90)
        self.textbox.resize(160, 30)

        self.show()

    def onClick(self):
        buttonReply = QMessageBox.question(self, 'Message', "Do you like PyQt5?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            self.textbox.setText("Yes clicked.")
        else:
            print('No clicked.')
            self.textbox.setText("No clicked.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
