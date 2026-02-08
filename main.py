import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = None


def main():
    app = App(sys.argv)
    
    # Создаём главное окно
    window = MainWindow()
    window.app = app  # ← Передаём ссылку на app в MainWindow
    app.main_window = window

    # Загружаем стиль по умолчанию
    # window.load_stylesheet("styles/light.css")

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
