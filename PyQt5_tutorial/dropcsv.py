#!/usr/bin/env python3

import sys
import os
from PyQt5.QtCore import pyqtSignal, QMimeData, Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QDialogButtonBox,
        QFrame, QLabel, QPushButton, QTableWidget, QTableWidgetItem,
        QVBoxLayout, QWidget, QHeaderView)

class DropArea(QLabel):

    changed = pyqtSignal(QMimeData)

    def __init__(self, parent = None):
        super(DropArea, self).__init__(parent)

        self.setMinimumSize(200, 100)
        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.setWordWrap(True)
        self.clear()

    def dragEnterEvent(self, event):
        print("dragEnterEvent")
        if (event.mimeData().hasFormat('text/uri-list')):
            event.acceptProposedAction()
            self.changed.emit(event.mimeData())

    def dropEvent(self, event):
        print("dropEvent")
        #mimeData = event.mimeData()
        #event.acceptProposedAction()

    def clear(self):
        print("clear")
        self.setText("<drop content>")


class DropWindow(QWidget):

    def __init__(self):
        super(DropWindow, self).__init__()

        self.label = QLabel("This example accepts drag csv file")
        self.label.setWordWrap(True)
        self.label.adjustSize()

        self.dropArea = DropArea()
        self.dropArea.changed.connect(self.updateTable)

        self.initTable()

        self.loadButton = QPushButton("Load")
        self.clearButton = QPushButton("Clear")
        self.quitButton = QPushButton("Quit")

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton(self.loadButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.clearButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.loadButton.pressed.connect(self.load)
        self.clearButton.pressed.connect(self.dropArea.clear)
        self.quitButton.pressed.connect(self.close)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.dropArea)
        mainLayout.addWidget(self.table)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Drop CSV")
        self.setMinimumSize(500, 500)
        self.move(50, 50)

    def updateTable(self, mimeData=None):
        print("updateTable")

        if mimeData is None:
            return

        urls = mimeData.urls()
        if len(urls) > 0:
            self.path = urls[0].toLocalFile()
            if (os.path.isfile(self.path)):
                print(self.path)
            self.dropArea.setText(self.path)

    def load(self):
        print('load')
        data = {'timestamp' : [], 'x' : [], 'y' : [], 'z' : [], 'qw' : [], 'qx' : [], 'qy' : [], 'qz' : []}
        f = open(self.path)
        for line in f.readlines():
            s = str.strip(line).split(',')
            print(s)
            data['timestamp'].append(int(s[0]))
            data['x'].append(float(s[1]))
            data['y'].append(float(s[2]))
            data['z'].append(float(s[3]))
            data['qw'].append(float(s[4]))
            data['qx'].append(float(s[5]))
            data['qy'].append(float(s[6]))
            data['qz'].append(float(s[7]))
        f.close

        self.table.setRowCount(0)
        for i in range(len(data['timestamp'])):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(str(data['timestamp'][i])))
            self.table.setItem(i, 1, QTableWidgetItem(str(data['x'][i])))
            self.table.setItem(i, 2, QTableWidgetItem(str(data['y'][i])))
            self.table.setItem(i, 3, QTableWidgetItem(str(data['z'][i])))
            self.table.setItem(i, 4, QTableWidgetItem(str(data['qw'][i])))
            self.table.setItem(i, 5, QTableWidgetItem(str(data['qx'][i])))
            self.table.setItem(i, 6, QTableWidgetItem(str(data['qy'][i])))
            self.table.setItem(i, 7, QTableWidgetItem(str(data['qz'][i])))

    def initTable(self):
        self.table = QTableWidget()

        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Timestamp", "x", "y", "z", 'qw', 'qx', 'qy', 'qz'])

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # 列寬設置
        self.table.horizontalHeader().setStretchLastSection(True); # 充滿列寬
        #self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch) # 行高設置
        #self.table.verticalHeader().setStretchLastSection(True); # 充滿行高

        self.table.setSelectionBehavior(QTableWidget.SelectRows) # 行選擇模式
        self.table.setSelectionMode(QAbstractItemView.SingleSelection); # 無法拖拽選擇

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DropWindow()
    window.show()
    sys.exit(app.exec_())
