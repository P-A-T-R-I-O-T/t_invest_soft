from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

# Импортируем наши меню
from ui.menus.file.file_main import FileMenu
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
        label = QLabel("Добро пожаловать в T-Invest!\nГотов к обучению и торговле? 🚀")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        central_widget.setLayout(layout)

        # Создаём меню
        menu_bar = self.menuBar()
        self.file_menu = FileMenu(menu_bar, self)        # ← создаём меню
        self.training_menu = TrainingMenu(menu_bar, self)
        self.trade_menu = TradeMenu(menu_bar, self)
        self.settings_menu = SettingsMenu(menu_bar, self)

    def load_stylesheet(self, path):
        """Загружает CSS из файла и применяет как стиль."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Ошибка загрузки стиля {path}: {e}")

