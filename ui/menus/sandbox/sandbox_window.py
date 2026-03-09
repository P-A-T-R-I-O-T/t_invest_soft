# ui/menus/sandbox/sandbox_window.py
# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QDialog)  # Заменили QWidget на QDialog

class SandboxSettingsWindow(QDialog):  # Наследуем от QDialog для отдельного окна
    def __init__(self, parent=None):
        super().__init__(parent)
        # Устанавливаем окно как независимое
        self.setWindowFlags(Qt.Window)
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(660, 378)

        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QRect(30, 10, 80, 20))

        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(30, 40, 120, 50))

        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 40, 61, 50))

        self.textEdit = QTextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(330, 44, 300, 71))
        self.textEdit.setReadOnly(True)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 10, 92, 24))

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 100, 41, 20))

        self.listWidget = QListWidget(self)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 130, 200, 150))

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 324, 79, 24))

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 290, 80, 24))

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 130, 140, 20))

        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(260, 160, 45, 20))

        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(260, 180, 45, 20))

        self.radioButton = QRadioButton(self)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(260, 200, 45, 20))

        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(430, 160, 200, 22))
        self.comboBox.setEditable(True)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 130, 70, 20))

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(480, 324, 150, 24))

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(260, 324, 150, 24))

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Настройки песочницы", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Баланс счёта", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Отображение баланса", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Валюта", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Отображение ТОКЕНА", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Показать токен", None))
        self.label.setText(QCoreApplication.translate("Form", u"Счета:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Удалить счёт", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Создать счёт", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Изменить валюту счёта", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"ERU", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"RUB", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"USD", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"сумма счёта", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Пополнить", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Применить", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Отменить все действия", None))



