# ui/menus/sandbox/sandbox_window

from PySide6.QtWidgets import (QDialog, QTabWidget, QVBoxLayout, QWidget,
                             QLabel, QTextEdit, QPushButton, QHBoxLayout,
                             QGridLayout, QLineEdit, QComboBox, QMessageBox, QApplication)
from PySide6.QtCore import Qt


class SandboxWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Песочница — T-Invest")
        self.resize(900, 600)
        self.setMinimumSize(700, 500)

        # Основной layout
        layout = QVBoxLayout()

        # Создаём виджет вкладок
        self.tab_widget = QTabWidget()
        self.setup_tabs()
        layout.addWidget(self.tab_widget)

        # Кнопки внизу
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def setup_tabs(self):
        """Создаёт и настраивает все вкладки."""
        # Вкладка 1: Тестирование стратегий
        self.strategy_tab = self.create_strategy_tab()
        self.tab_widget.addTab(self.strategy_tab, "Тестирование стратегий")

        # Вкладка 2: Моделирование сделок
        self.trade_sim_tab = self.create_trade_simulation_tab()
        self.tab_widget.addTab(self.trade_sim_tab, "Моделирование сделок")

        # Вкладка 3: Анализ данных
        self.analysis_tab = self.create_analysis_tab()
        self.tab_widget.addTab(self.analysis_tab, "Анализ данных")

        # Вкладка 4: Настройки песочницы
        self.settings_tab = self.create_settings_tab()
        self.tab_widget.addTab(self.settings_tab, "Настройки")

    def create_strategy_tab(self):
        """Создаёт вкладку для тестирования торговых стратегий."""
        tab = QWidget()
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

        tab.setLayout(layout)
        return tab

    def create_trade_simulation_tab(self):
        """Создаёт вкладку для моделирования сделок."""
        tab = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Моделирование сделок")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        desc = QLabel("Практикуйтесь в совершении сделок с виртуальными деньгами.")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # Имитация биржевого стакана
        order_book_label = QLabel("Биржевой стакан (имитация):")
        layout.addWidget(order_book_label)

        self.order_book = QTextEdit()
        self.order_book.setPlainText(
"""Лучшие заявки на покупку:
- 100 акций по 150.50 руб.
- 50 акций по 150.45 руб.
- 200 акций по 150.40 руб.

Лучшие заявки на продажу:
- 150 акций по 150.60 руб.
- 75 акций по 150.65 руб.
- 300 акций по 150.70 руб."""
        )
        self.order_book.setMaximumHeight(150)
        layout.addWidget(self.order_book)

        # Форма для создания сделки
        trade_form = QGridLayout()

        trade_form.addWidget(QLabel("Тип сделки:"), 0, 0)
        self.trade_type = QComboBox()
        self.trade_type.addItems(["Покупка", "Продажа"])
        trade_form.addWidget(self.trade_type, 0, 1)

        trade_form.addWidget(QLabel("Количество акций:"), 1, 0)
        self.shares_input = QLineEdit("10")
        trade_form.addWidget(self.shares_input, 1, 1)

        trade_form.addWidget(QLabel("Цена за акцию:"), 2, 0)
        self.price_input = QLineEdit("150.55")
        trade_form.addWidget(self.price_input, 2, 1)

        layout.addLayout(trade_form)

        execute_btn = QPushButton("Выполнить сделку")
        execute_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 8px;")
        execute_btn.clicked.connect(self.execute_trade)
        layout.addWidget(execute_btn)

            # Область для отображения истории сделок
        self.trade_history = QTextEdit()
        self.trade_history.setPlaceholderText("История сделок будет отображаться здесь...")
        self.trade_history.setMaximumHeight(200)
        layout.addWidget(QLabel("История сделок:"))
        layout.addWidget(self.trade_history)

        tab.setLayout(layout)
        return tab

    def execute_trade(self):
        """Обрабатывает выполнение виртуальной сделки."""
        try:
            trade_type = self.trade_type.currentText()
            shares = int(self.shares_input.text())
            price = float(self.price_input.text().replace(',', '.'))
            total_amount = shares * price

            # Формируем запись о сделке
            trade_record = f"{trade_type}: {shares} акций по {price:.2f} руб. = {total_amount:.2f} руб."

            # Добавляем в историю сделок
            current_history = self.trade_history.toPlainText()
            if current_history:
                self.trade_history.setPlainText(current_history + "\n" + trade_record)
            else:
                self.trade_history.setPlainText(trade_record)

            # Показываем уведомление об успешной сделке
            QMessageBox.information(
                self,
                "Сделка выполнена",
                f"Успешно выполнена виртуальная {trade_type.lower()}!\n"
                f"Количество: {shares} акций\n"
                f"Цена: {price:.2f} руб.\n"
                f"Сумма: {total_amount:.2f} руб."
            )

        except ValueError as e:
            QMessageBox.warning(
                self,
                "Ошибка ввода",
                "Проверьте корректность введённых данных:\n"
                "Количество акций должно быть целым числом,\n"
                "Цена должна быть числом (можно с дробной частью)."
            )

    def create_analysis_tab(self):
        """Создаёт вкладку для анализа данных."""
        tab = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Анализ данных")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        desc = QLabel(
            "Анализируйте результаты тестирования стратегий и моделирования сделок.\n"
            "Визуализация данных поможет улучшить ваши торговые решения."
        )
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # Область для графиков (заглушка — в реальной реализации нужно добавить matplotlib)
        graph_label = QLabel("Область для графиков (в разработке)")
        graph_label.setAlignment(Qt.AlignCenter)
        graph_label.setStyleSheet("background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc;")
        layout.addWidget(graph_label)

        # Форма для выбора типа анализа
        analysis_form = QGridLayout()

        analysis_form.addWidget(QLabel("Тип анализа:"), 0, 0)
        self.analysis_type = QComboBox()
        self.analysis_type.addItems([
            "Доходность по стратегиям",
            "Распределение сделок по времени",
            "Анализ рисков",
            "Сравнение с бенчмарком"
        ])
        analysis_form.addWidget(self.analysis_type, 0, 1)

        layout.addLayout(analysis_form)

        analyze_btn = QPushButton("Выполнить анализ")
        analyze_btn.setStyleSheet("background-color: #9C27B0; color: white; padding: 8px;")
        analyze_btn.clicked.connect(self.run_analysis)
        layout.addWidget(analyze_btn)

        # Область для вывода результатов анализа
        self.analysis_results = QTextEdit()
        self.analysis_results.setPlaceholderText("Результаты анализа будут отображены здесь...")
        self.analysis_results.setMaximumHeight(250)
        layout.addWidget(QLabel("Результаты анализа:"))
        layout.addWidget(self.analysis_results)

        tab.setLayout(layout)
        return tab

    def run_analysis(self):
        """Выполняет выбранный тип анализа."""
        analysis_type = self.analysis_type.currentText()
        result = f"Выполняется анализ: {analysis_type}\n\n"
        result += "Пример результатов:\n"
        result += "- Общая доходность: +15.6%\n"
        result += "- Максимальная просадка: -8.2%\n"
        result += "- Коэффициент Шарпа: 1.45\n"
        result += "- Количество прибыльных сделок: 68%"

        self.analysis_results.setPlainText(result)

    def create_settings_tab(self):
        """Создаёт вкладку настроек песочницы."""
        tab = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Настройки песочницы")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        # Настройки симуляции
        settings_form = QGridLayout()

        settings_form.addWidget(QLabel("Режим симуляции:"), 0, 0)
        self.simulation_mode = QComboBox()
        self.simulation_mode.addItems(["Реальное время", "Ускоренное время", "По шагам"])
        settings_form.addWidget(self.simulation_mode, 0, 1)

        settings_form.addWidget(QLabel("Комиссии (%):"), 1, 0)
        self.commission_input = QLineEdit("0.05")
        settings_form.addWidget(self.commission_input, 1, 1)

        settings_form.addWidget(QLabel("Спред (%):"), 2, 0)
        self.spread_input = QLineEdit("0.1")
        settings_form.addWidget(self.spread_input, 2, 1)

        layout.addLayout(settings_form)

        # Кнопки сохранения/сброса
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Сохранить настройки")
        save_btn.setStyleSheet("background-color: #FF9800; color: white; padding: 8px;")
        save_btn.clicked.connect(self.save_settings)
        button_layout.addWidget(save_btn)

        reset_btn = QPushButton("Сбросить к умолчанию")
        reset_btn.setStyleSheet("background-color: #757575; color: white; padding: 8px;")
        reset_btn.clicked.connect(self.reset_settings)
        button_layout.addWidget(reset_btn)

        layout.addLayout(button_layout)

        # Область статуса
        self.settings_status = QLabel("Настройки готовы к сохранению")
        self.settings_status.setStyleSheet("color: #666;")
        layout.addWidget(self.settings_status)

        tab.setLayout(layout)
        return tab

    def save_settings(self):
        """Сохраняет настройки песочницы."""
        self.show_info_message(
            "Настройки сохранены",
            "Настройки песочницы успешно сохранены!"
        )
        self.settings_status.setText("Настройки успешно сохранены!")
        self.settings_status.setStyleSheet("color: #4CAF50;")

    def reset_settings(self):
        """Сбрасывает настройки к значениям по умолчанию."""
        self.simulation_mode.setCurrentIndex(0)
        self.commission_input.setText("0.05")
        self.spread_input.setText("0.1")
        self.settings_status.setText("Настройки сброшены к значениям по умолчанию")
        self.settings_status.setStyleSheet("color: #2196F3;")

    def run_strategy_test(self):
        """Запускает тестирование торговой стратегии."""
        try:
            strategy_name = self.strategy_name.text().strip()
            if not strategy_name:
                self.show_warning_message("Ошибка", "Введите название стратегии")
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
            self.show_warning_message(
                "Ошибка ввода",
                "Проверьте корректность введённых данных:\n"
                "Начальный капитал должен быть числом."
            )