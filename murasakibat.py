# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 382)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.textEdit)

        self.toolBar = QGroupBox(self.groupBox)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.toolBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.userInput = QLineEdit(self.toolBar)
        self.userInput.setObjectName(u"userInput")
        sizePolicy1.setHeightForWidth(self.userInput.sizePolicy().hasHeightForWidth())
        self.userInput.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.userInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.excuteButton = QPushButton(self.toolBar)
        self.excuteButton.setObjectName(u"excuteButton")
        sizePolicy1.setHeightForWidth(self.excuteButton.sizePolicy().hasHeightForWidth())
        self.excuteButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.excuteButton)

        self.downloadButton = QPushButton(self.toolBar)
        self.downloadButton.setObjectName(u"downloadButton")
        sizePolicy1.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.downloadButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addWidget(self.toolBar)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6bdb\u56fe", None))
        self.userInput.setText("")
        self.excuteButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
    # retranslateUi

