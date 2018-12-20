#!/usr/bin/env python3

import sys
import os
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QDialogButtonBox,
        QLabel, QPushButton, QVBoxLayout, QWidget)
from PyQt5 import QtCore

class MyWidget(QWidget):

    def __init__(self):
        super(MyWidget, self).__init__()

        self.setWindowTitle('Timer')
        self.setMinimumSize(500, 500)
        self.move(50, 50)

        self.label = QLabel('This timer example')

        self.startButton = QPushButton('Start')
        self.stopButton = QPushButton('Stop')
        self.quitButton = QPushButton('Quit')

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton(self.startButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.stopButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.quitButton.clicked.connect(self.close)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def start(self):
        print('start')
        self.timer_id = self.startTimer(500) # timer of QWidget
        
        # create a timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent2)
        self.timer.start(500)

    def stop(self):
        print('stop')
        self.killTimer(self.timer_id)

        self.timer.stop()

    def timerEvent(self, event):
        print('timerEvent')

    def timerEvent2(self):
        print('timerEvent2')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
