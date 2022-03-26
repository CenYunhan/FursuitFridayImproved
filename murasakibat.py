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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(288, 457)
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
        self.gridLayout = QGridLayout(self.toolBar)
        self.gridLayout.setObjectName(u"gridLayout")
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


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.comboBox = QComboBox(self.toolBar)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboBox, 6, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.toolBar)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.userInput = QLineEdit(self.groupBox_2)
        self.userInput.setObjectName(u"userInput")
        sizePolicy1.setHeightForWidth(self.userInput.sizePolicy().hasHeightForWidth())
        self.userInput.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.userInput)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.toolBar)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.URLAddress = QLineEdit(self.groupBox_3)
        self.URLAddress.setObjectName(u"URLAddress")
        sizePolicy1.setHeightForWidth(self.URLAddress.sizePolicy().hasHeightForWidth())
        self.URLAddress.setSizePolicy(sizePolicy1)
        self.URLAddress.setMinimumSize(QSize(128, 0))
        self.URLAddress.setDragEnabled(False)

        self.horizontalLayout_3.addWidget(self.URLAddress)


        self.gridLayout.addWidget(self.groupBox_3, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.toolBar)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6bdb\u56fe", None))
        self.toolBar.setTitle("")
        self.excuteButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u8bf7\u9009\u62e9\u6d4f\u89c8\u5668--", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Microsoft Edge", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Google Chrome", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Apple Safari", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.userInput.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"URL", None))
        self.URLAddress.setText(QCoreApplication.translate("MainWindow", u"https://t.bilibili.com/topic/8807683/", None))
    # retranslateUi

