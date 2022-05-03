# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 556)
        self.action_download = QAction(MainWindow)
        self.action_download.setObjectName(u"action_download")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_1 = QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy2)
        self.checkBox_1.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_5.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy2)
        self.checkBox_2.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_5.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy2.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy2)
        self.checkBox_3.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_5.addWidget(self.checkBox_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy2.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy2)
        self.checkBox_7.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_6.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy2.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy2)
        self.checkBox_8.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_6.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy2.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy2)
        self.checkBox_9.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_6.addWidget(self.checkBox_9)


        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem.setCheckState(0, Qt.Unchecked);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.treeWidget, 9, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_9)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy2.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy2)
        self.checkBox_4.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_7.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy2.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy2)
        self.checkBox_5.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_7.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy2.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy2)
        self.checkBox_6.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_7.addWidget(self.checkBox_6)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")

        self.horizontalLayout_4.addWidget(self.prev_button)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout_4.addWidget(self.next_button)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 476, 24))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(446, 259, 99, 110))
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_download)
        self.menu.addAction(self.actionclose)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.action_download.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d", None))
#if QT_CONFIG(shortcut)
        self.action_download.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
#if QT_CONFIG(accessibility)
        self.menuBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

