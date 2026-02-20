from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

# Импортируем наши меню
from ui.menus.file.file_main import FileMenu
from ui.menus.sandbox.sandbox_window import SandboxWindow
from ui.menus.training.training import TrainingMenu
from ui.menus.trade.trade import TradeMenu
from ui.menus.settings.settings import SettingsMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T-Invest")
        self.resize(800, 600)
        self.setMinimumSize(400, 300)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        label = QLabel("Добро пожаловать в T-Invest!\nГотов к обучению и торговле? 🦮")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        central_widget.setLayout(layout)

        # Создаём меню
        menu_bar = self.menuBar()

        # 1. Создаём FileMenu (пункт «Файл»)
        self.file_menu = FileMenu(menu_bar, self)

        # 2. Добавляем пункт «Песочница» сразу после «Файл»
        sandbox_action = QAction("Песочница", self)
        sandbox_action.triggered.connect(self.open_sandbox)
        menu_bar.addAction(sandbox_action)

        # 3. Создаём остальные меню (они появятся после «Песочницы API»)
        self.training_menu = TrainingMenu(menu_bar, self)
        self.trade_menu = TradeMenu(menu_bar, self)
        self.settings_menu = SettingsMenu(menu_bar, self)

        # Храним экземпляр окна песочницы (изначально None)
        self.sandbox_window = None

    def open_sandbox(self):
        """Открывает окно песочницы"""
        if self.sandbox_window is None:
            self.sandbox_window = SandboxWindow(self)
        self.sandbox_window.show()
        self.sandbox_window.raise_() # Выносим на передний план
        self.sandbox_window.activateWindow() # Фокусируем

    def load_stylesheet(self, path):
        """Загружает CSS из файла и применяет как стиль."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Ошибка загрузки стиля {path}: {e}")