from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit, QGridLayout
from ..utils.message_utils import show_warning_message

class StrategyTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Тестирование торговых стратегий")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        desc = QLabel("Здесь вы можете тестировать свои торговые стратегии на исторических данных без риска.")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # Форма для ввода параметров стратегии
        form_layout = QGridLayout()

        form_layout.addWidget(QLabel("Название стратегии:"), 0, 0)
        self.strategy_name = QLineEdit()
        form_layout.addWidget(self.strategy_name, 0, 1)

        form_layout.addWidget(QLabel("Период тестирования:"), 1, 0)
        self.period_combo = QComboBox()
        self.period_combo.addItems(["1 месяц", "3 месяца", "6 месяцев", "1 год", "2 года"])
        form_layout.addWidget(self.period_combo, 1, 1)

        form_layout.addWidget(QLabel("Начальный капитал:"), 2, 0)
        self.capital_input = QLineEdit("100000")
        form_layout.addWidget(self.capital_input, 2, 1)

        layout.addLayout(form_layout)

        # Кнопка запуска тестирования
        test_btn = QPushButton("Запустить тестирование")
        test_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        test_btn.clicked.connect(self.run_strategy_test)
        layout.addWidget(test_btn)

        # Область для вывода результатов
        self.results_display = QTextEdit()
        self.results_display.setPlaceholderText("Результаты тестирования будут отображены здесь...")
        self.results_display.setMaximumHeight(200)
        layout.addWidget(QLabel("Результаты тестирования:"))
        layout.addWidget(self.results_display)

        self.setLayout(layout)

    def run_strategy_test(self):
        """Запускает тестирование торговой стратегии."""
        try:
            strategy_name = self.strategy_name.text().strip()
            if not strategy_name:
                show_warning_message("Ошибка", "Введите название стратегии")
                return

            period = self.period_combo.currentText()
            capital = float(self.capital_input.text().replace(',', '.'))

            # Базовая симуляция тестирования
            result = (
                f"Результаты тестирования стратегии: {strategy_name}\n\n"
                f"Период: {period}\n"
                f"Начальный капитал: {capital:,.2f} руб.\n\n"
                "--- Результаты симуляции ---\n"
                "- Общая доходность: +12.5%\n"
                "- Количество сделок: 45\n"
                "- Прибыльных сделок: 65%\n"
                "- Максимальная просадка: -7.3%\n"
                "- Коэффициент Шарпа: 1.2"
            )
            self.results_display.setPlainText(result)

        except ValueError:
            show_warning_message(
                "Ошибка ввода",
                "Проверьте корректность введённых данных:\n"
                "Начальный капитал должен быть числом."
            )
