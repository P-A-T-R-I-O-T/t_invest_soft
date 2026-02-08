# widgets_for_selection.py
# Примеры всех виджетов PySide6 для выбора из списка

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QCheckBox, QRadioButton, QListWidget, QComboBox,
    QPushButton, QLabel, QGroupBox, QButtonGroup,
    QAbstractItemView, QFrame, QGridLayout
)
from PySide6.QtCore import Qt


class SelectionWidgetsDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Виджеты выбора в PySide6")
        self.resize(700, 600)

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        # === 1. QCheckBox — выбор нескольких вариантов (галочки) ===
        group1 = self.create_groupbox("1. QCheckBox — множественный выбор (галочки)")
        layout1 = QVBoxLayout()

        self.checkbox_fruit = QCheckBox("Яблоко")
        self.checkbox_fruit.setChecked(True)  # можно задать начальное состояние
        self.checkbox_fruit.toggled.connect(self.show_status)

        self.checkbox_veg = QCheckBox("Морковь")
        self.checkbox_veg.toggled.connect(self.show_status)

        self.checkbox_berry = QCheckBox("Клубника")
        self.checkbox_berry.toggled.connect(self.show_status)

        layout1.addWidget(self.checkbox_fruit)
        layout1.addWidget(self.checkbox_veg)
        layout1.addWidget(self.checkbox_berry)

        group1.setLayout(layout1)
        main_layout.addWidget(group1)

        # === 2. QRadioButton — выбор одного из нескольких (радиокнопки) ===
        group2 = self.create_groupbox("2. QRadioButton — выбор одного варианта")
        layout2 = QVBoxLayout()

        # Группа радиокнопок: только одна может быть выбрана
        self.radio_group = QButtonGroup(self)
        self.radio_red = QRadioButton("Красный")
        self.radio_green = QRadioButton("Зелёный")
        self.radio_blue = QRadioButton("Синий")
        self.radio_green.setChecked(True)  # выбран по умолчанию

        # Добавляем в QButtonGroup для связи
        self.radio_group.addButton(self.radio_red)
        self.radio_group.addButton(self.radio_green)
        self.radio_group.addButton(self.radio_blue)

        # Подключаем сигнал
        self.radio_group.buttonToggled.connect(self.show_status)

        layout2.addWidget(self.radio_red)
        layout2.addWidget(self.radio_green)
        layout2.addWidget(self.radio_blue)

        group2.setLayout(layout2)
        main_layout.addWidget(group2)

        # === 3. QListWidget — выбор из списка (один или несколько) ===
        group3 = self.create_groupbox("3. QListWidget — выбор из списка")
        layout3 = QGridLayout()

        # Подпись
        layout3.addWidget(QLabel("Выберите один или несколько:"), 0, 0, 1, 2)

        # Список
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Апельсин", "Банан", "Виноград", "Ананас"])
        self.list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Ctrl/Shift для множества
        self.list_widget.itemSelectionChanged.connect(self.show_status)

        # Режимы выбора
        self.btn_single = QPushButton("Один")
        self.btn_multi = QPushButton("Несколько")
        self.btn_single.clicked.connect(lambda: self.set_list_selection_mode("single"))
        self.btn_multi.clicked.connect(lambda: self.set_list_selection_mode("multi"))

        layout3.addWidget(self.list_widget, 1, 0, 1, 2)
        layout3.addWidget(self.btn_single, 2, 0)
        layout3.addWidget(self.btn_multi, 2, 1)

        group3.setLayout(layout3)
        main_layout.addWidget(group3)

        # === 4. QComboBox — выпадающий список (один выбор) ===
        group4 = self.create_groupbox("4. QComboBox — один выбор из выпадающего списка")
        layout4 = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Москва", "Питер", "Новосибирск", "Екатеринбург"])
        self.combo.currentTextChanged.connect(self.show_status)

        layout4.addWidget(QLabel("Город:"))
        layout4.addWidget(self.combo)
        group4.setLayout(layout4)
        main_layout.addWidget(group4)

        # === 5. Кастомный QComboBox с чекбоксами (множественный выбор) ===
        group5 = self.create_groupbox("5. QComboBox с множественным выбором (как в фильтрах)")
        layout5 = QVBoxLayout()

        # Эмуляция "выбора нескольких" через QLineEdit + кнопку
        self.combo_multi_line = QLabel("Не выбрано")
        self.combo_multi_btn = QPushButton("Выбрать теги...")
        self.combo_multi_btn.clicked.connect(self.open_tags_dialog)

        layout5.addWidget(QLabel("Теги (множественный выбор):"))
        layout5.addWidget(self.combo_multi_line)
        layout5.addWidget(self.combo_multi_btn)

        group5.setLayout(layout5)
        main_layout.addWidget(group5)

        # === Область вывода ===
        self.result_label = QLabel("Состояние: —")
        self.result_label.setFrameStyle(QFrame.Box)
        self.result_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        # Инициализация состояния
        self.show_status()

    def create_groupbox(self, title):
        """Унифицированное создание групп"""
        group = QGroupBox(title)
        group.setStyleSheet("QGroupBox { font-weight: bold; padding: 10px; }")
        return group

    def show_status(self):
        """Отображает текущий выбор всех виджетов"""
        parts = []

        # 1. Чекбоксы
        selected_checks = []
        if self.checkbox_fruit.isChecked():
            selected_checks.append("Яблоко")
        if self.checkbox_veg.isChecked():
            selected_checks.append("Морковь")
        if self.checkbox_berry.isChecked():
            selected_checks.append("Клубника")
        parts.append(f"Галочки: {', '.join(selected_checks) if selected_checks else 'ничего'}")

        # 2. Радиокнопки
        radio_selected = self.radio_group.checkedButton()
        if radio_selected:
            parts.append(f"Цвет: {radio_selected.text()}")
        else:
            parts.append("Цвет: не выбран")

        # 3. Список
        list_selected = [item.text() for item in self.list_widget.selectedItems()]
        parts.append(f"Список: {', '.join(list_selected) if list_selected else 'ничего'}")

        # 4. Комбобокс
        combo_text = self.combo.currentText()
        parts.append(f"Город: {combo_text}")

        self.result_label.setText(" | ".join(parts))

    def set_list_selection_mode(self, mode):
        """Меняет режим выбора в QListWidget"""
        if mode == "single":
            self.list_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        else:
            self.list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def open_tags_dialog(self):
        """Простой диалог для множественного выбора (как в фильтрах)"""
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox

        dialog = QDialog(self)
        dialog.setWindowTitle("Выберите теги")
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Выберите интересующие темы:"))

        # Чекбоксы в диалоге
        tags = ["Python", "Дизайн", "Музыка", "Спорт", "Книги"]
        checkboxes = []
        for tag in tags:
            cb = QCheckBox(tag)
            if tag in self.combo_multi_line.text():
                cb.setChecked(True)
            layout.addWidget(cb)
            checkboxes.append(cb)

        # Кнопки
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        dialog.setLayout(layout)

        if dialog.exec():
            selected = [cb.text() for cb in checkboxes if cb.isChecked()]
            self.combo_multi_line.setText(", ".join(selected) if selected else "Не выбрано")


# === Запуск приложения ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectionWidgetsDemo()
    window.show()
    sys.exit(app.exec())
