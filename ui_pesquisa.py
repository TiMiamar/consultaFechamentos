# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pesquisa.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDateTimeEdit,
    QDialog, QLabel, QLineEdit, QListView,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(444, 395)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(11, 329, 62, 20))
        self.radioButton.setTabletTracking(False)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(11, 275, 111, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(11, 302, 85, 20))
        self.radioButton_3.setTabletTracking(False)
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoRepeat(False)
        self.radioButton_3.setAutoExclusive(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(11, 356, 431, 28))
        self.dateEdit_2 = QDateEdit(Dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(11, 178, 101, 24))
        self.dateEdit_2.setWrapping(False)
        self.dateEdit_2.setFrame(True)
        self.dateEdit_2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_2.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setCurrentSectionIndex(0)
        self.dateEdit_2.setTimeSpec(Qt.LocalTime)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(11, 244, 101, 24))
        self.dateEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(11, 112, 137, 24))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(11, 46, 137, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 11, 67, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 77, 61, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 143, 63, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 209, 57, 16))
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(160, 30, 271, 311))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Todos", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"N\u00e3o Conciliado", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Conciliado", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Pesquisar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Valor Inicial", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Valor Final", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Data Inicial", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Data Final", None))
    # retranslateUi

