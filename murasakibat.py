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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(740, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_5.addWidget(self.textEdit)

        self.toolBar = QGroupBox(self.groupBox)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.toolBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.userInput = QLineEdit(self.toolBar)
        self.userInput.setObjectName(u"userInput")
        sizePolicy.setHeightForWidth(self.userInput.sizePolicy().hasHeightForWidth())
        self.userInput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.userInput)

        self.excuteButton = QPushButton(self.toolBar)
        self.excuteButton.setObjectName(u"excuteButton")
        sizePolicy.setHeightForWidth(self.excuteButton.sizePolicy().hasHeightForWidth())
        self.excuteButton.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.excuteButton)


        self.verticalLayout_5.addWidget(self.toolBar)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.userInput.setText("")
        self.excuteButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

