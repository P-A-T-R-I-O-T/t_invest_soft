# ui/menus/sandbox/create_account.py
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QPushButton, QGroupBox,
    QRadioButton, QDoubleSpinBox, QCheckBox
)

class CreateAccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Создание счёта")
        self.resize(300, 250)
        self._init_ui()

    def _init_ui(self):
        """Инициализация и размещение всех элементов интерфейса."""
        layout = QVBoxLayout()

        # Поле ввода названия счёта
        layout.addWidget(QLabel("Название счёта:"))
        self.account_name_input = QLineEdit()
        self.account_name_input.setPlaceholderText("Мой тестовый счёт")
        layout.addWidget(self.account_name_input)

        # Группа выбора валюты
        currency_group = QGroupBox("Выберите валюту")
        currency_layout = QHBoxLayout()

        self.usd_radio = QRadioButton("USD")
        self.eur_radio = QRadioButton("EUR")
        self.rub_radio = QRadioButton("RUB")
        self.rub_radio.setChecked(True)  # По умолчанию RUB

        currency_layout.addWidget(self.usd_radio)
        currency_layout.addWidget(self.eur_radio)
        currency_layout.addWidget(self.rub_radio)
        currency_group.setLayout(currency_layout)
        layout.addWidget(currency_group)

        # Поле для указания суммы (используем DoubleSpinBox для чисел)
        layout.addWidget(QLabel("Начальный баланс:"))
        self.balance_spin = QDoubleSpinBox()
        self.balance_spin.setRange(0, 1_000_000)
        self.balance_spin.setDecimals(2)
        self.balance_spin.setValue(0.0)
        layout.addWidget(self.balance_spin)

        # Чекбокс для особых условий
        self.special_checkbox = QCheckBox("Для песочницы (автоматически)")
        self.special_checkbox.setChecked(True)
        self.special_checkbox.setEnabled(False)  # Делаем неактивным, т.к. всегда песочница
        layout.addWidget(self.special_checkbox)

        # Кнопки
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        self.create_button = QPushButton("Создать")
        self.cancel_button = QPushButton("Отмена")
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Сигналы
        self.create_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_data(self) -> dict:
        """Возвращает введённые данные."""
        return {
            'name': self.account_name_input.text().strip(),
            'currency': self._get_selected_currency(),
            'initial_balance': self.balance_spin.value()
        }

    def _get_selected_currency(self) -> str:
        """Возвращает выбранную валюту или пустую строку, если ничего не выбрано."""
        if self.usd_radio.isChecked():
            return "USD"
        elif self.eur_radio.isChecked():
            return "EUR"
        elif self.rub_radio.isChecked():
            return "RUB"
        return ""

