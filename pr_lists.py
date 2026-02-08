# Импорт необходимых модулей PySide6
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QListView, QComboBox,
    QPushButton, QLineEdit, QLabel, QTreeView, QTableView,
    QAbstractItemView, QGroupBox, QFormLayout
)
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys


class ListExamplesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Примеры списков в PySide6")
        self.resize(600, 500)

        layout = QVBoxLayout()

        # === 1. QListWidget — простой список с элементами ===
        group1 = QGroupBox("1. QListWidget — простой список")
        layout1 = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.addItems(["Яблоко", "Банан", "Апельсин"])
        self.list_widget.addItem(QListWidgetItem("Виноград"))  # Можно добавлять объекты
        self.list_widget.setCurrentRow(0)  # Выделить первый элемент

        layout1.addWidget(QLabel("Простой список с возможностью выбора:"))
        layout1.addWidget(self.list_widget)
        group1.setLayout(layout1)
        layout.addWidget(group1)

        # === 2. QListView с QStringListModel — модельный подход ===
        group2 = QGroupBox("2. QListView + QStringListModel")
        layout2 = QVBoxLayout()

        self.string_list = ["Кот", "Собака", "Попугай"]
        self.string_model = QStringListModel(self.string_list)

        self.list_view = QListView()
        self.list_view.setModel(self.string_model)
        self.list_view.setSelectionMode(QAbstractItemView.SingleSelection)

        layout2.addWidget(QLabel("Список на основе модели (удобно для больших данных):"))
        layout2.addWidget(self.list_view)
        group2.setLayout(layout2)
        layout.addWidget(group2)

        # === 3. QComboBox — выпадающий список ===
        group3 = QGroupBox("3. QComboBox — выпадающий список")
        layout3 = QHBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Красный", "Зелёный", "Синий"])
        self.combo.setCurrentIndex(0)

        self.combo_label = QLabel("Выбрано: Красный")
        self.combo.currentTextChanged.connect(self.update_combo_label)

        layout3.addWidget(QLabel("Цвета:"))
        layout3.addWidget(self.combo)
        layout3.addWidget(self.combo_label)
        group3.setLayout(layout3)
        layout.addWidget(group3)

        # === 4. QTreeView — иерархический список (дерево) ===
        group4 = QGroupBox("4. QTreeView — иерархический список")
        layout4 = QVBoxLayout()

        self.tree_model = QStandardItemModel()
        self.tree_model.setHorizontalHeaderLabels(["Животные"])

        root = self.tree_model.invisibleRootItem()

        mammals = QStandardItem("Млекопитающие")
        mammals.appendRow(QStandardItem("Лев"))
        mammals.appendRow(QStandardItem("Тигр"))

        birds = QStandardItem("Птицы")
        birds.appendRow(QStandardItem("Орёл"))
        birds.appendRow(QStandardItem("Попугай"))

        root.appendRow(mammals)
        root.appendRow(birds)

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandAll()  # Раскрыть всё

        layout4.addWidget(QLabel("Дерево с вложенными элементами:"))
        layout4.addWidget(self.tree_view)
        group4.setLayout(layout4)
        layout.addWidget(group4)

        # === 5. QTableView — табличный список (тоже модель) ===
        group5 = QGroupBox("5. QTableView — табличный список")
        layout5 = QVBoxLayout()

        self.table_model = QStandardItemModel(3, 2)
        self.table_model.setHorizontalHeaderLabels(["Имя", "Возраст"])

        self.table_model.setItem(0, 0, QStandardItem("Анна"))
        self.table_model.setItem(0, 1, QStandardItem("25"))
        self.table_model.setItem(1, 0, QStandardItem("Борис"))
        self.table_model.setItem(1, 1, QStandardItem("30"))

        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        self.table_view.horizontalHeader().setStretchLastSection(True)

        layout5.addWidget(QLabel("Таблица как список строк:"))
        layout5.addWidget(self.table_view)
        group5.setLayout(layout5)
        layout.addWidget(group5)

        # === Управление: добавление элемента в QListWidget ===
        control_layout = QFormLayout()
        self.new_item_input = QLineEdit()
        self.add_button = QPushButton("Добавить в QListWidget")
        self.add_button.clicked.connect(self.add_to_list_widget)

        control_layout.addRow("Новый элемент:", self.new_item_input)
        control_layout.addWidget(self.add_button)
        layout.addLayout(control_layout)

        self.setLayout(layout)

    def update_combo_label(self, text):
        self.combo_label.setText(f"Выбрано: {text}")

    def add_to_list_widget(self):
        text = self.new_item_input.text().strip()
        if text:
            self.list_widget.addItem(text)
            self.new_item_input.clear()


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListExamplesWindow()
    window.show()
    sys.exit(app.exec())
