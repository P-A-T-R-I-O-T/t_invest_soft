# test_sandbox.py

import sys
from PySide6.QtWidgets import QApplication
from sandbox_window import Ui_Form
from PySide6.QtWidgets import QWidget

class TestSandboxWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Создаём экземпляр UI
        self.ui = Ui_Form()
        # Применяем UI к текущему виджету
        self.ui.setupUi(self)

def main():
    # Создаём приложение Qt
    app = QApplication(sys.argv)

    # Создаём и показываем тестовое окно
    window = TestSandboxWindow()
    window.show()

    # Запускаем главный цикл приложения
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
