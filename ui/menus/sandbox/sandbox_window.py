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
    QTextEdit, QDialog, QLineEdit)
#from ui.menus.sandbox.create_account import CreateAccountDialog


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

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 290, 80, 24))

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 160, 140, 20))

        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(260, 190, 45, 20))

        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(260, 212, 45, 20))

        self.radioButton = QRadioButton(self)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(260, 234, 45, 20))

        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(430, 232, 200, 22))
        self.comboBox.setEditable(True)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 212, 70, 20))

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(480, 324, 150, 24))

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(260, 324, 150, 24))

        self.radioButton_4 = QRadioButton(self)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(260, 130, 81, 20))

        self.radioButton_5 = QRadioButton(self)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(430, 130, 71, 20))

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(430, 180, 200, 22))

        self.label_7 = QLabel(self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 160, 90, 20))

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(385, 274, 90, 24))

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Баланс счёта", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Отображение баланса", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Валюта", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Отображение ТОКЕНА", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Показать токен", None))
        self.label.setText(QCoreApplication.translate("Form", u"Счета:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Удалить счёт", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Изменить валюту счёта", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"ERU", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"RUB", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"USD", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"сумма счёта", None))
        self.comboBox.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Пополнить", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Применить", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Отменить все действия", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"Изменить", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"Создать", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Введите имя счёта", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Название счёта", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Изменить счёт", None))


    def update_accounts_list(self):
        """Обновляет список счетов в listWidget."""
        # Получаем настройки песочницы из родительского окна
        sandbox_settings = self.parent().sandbox_settings

        if not sandbox_settings or not sandbox_settings.is_connected():
            self.listWidget.clear()
            self.listWidget.addItem("❌ Не подключено к песочнице")
            return

        # Получаем список счетов через API
        accounts = sandbox_settings.get_accounts_list()

        if accounts is None:
            self.listWidget.clear()
            self.listWidget.addItem("❌ Ошибка при получении списка счетов")
            return

        # Очищаем текущий список
        self.listWidget.clear()

        # Заполняем listWidget данными о счетах
        for account in accounts:
            item_text = f"{account.broker_account_id} ({account.status})"
            self.listWidget.addItem(item_text)

    def showEvent(self, event):
        """Переопределяем событие показа окна — вызываем обновление списка счетов."""
        super().showEvent(event)
        self.update_accounts_list()

    def open_create_account_dialog(self):
        """Открывает диалог создания счёта."""
        dialog = CreateAccountDialog(self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()
            sandbox_settings = self.parent().sandbox_settings

            if not sandbox_settings:
                self.listWidget.addItem("❌ Настройки песочницы не инициализированы")
                return

            # Создаём счёт через API
            new_account = sandbox_settings.create_sandbox_account(
                currency=data['currency'],
                initial_balance=data['initial_balance'],
                name=data['name']
            )

            if new_account:
                # Обновляем список счетов сразу после создания
                self.update_accounts_list()
                print(f"✅ Счёт создан: {new_account['id']} ({new_account['status']})")
            else:
                self.listWidget.addItem("❌ Ошибка при создании счёта")



