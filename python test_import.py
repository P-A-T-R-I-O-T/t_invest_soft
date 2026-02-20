try:
    from PySide6.QtWidgets import QAction, QMainWindow
    print("✓ QAction успешно импортирован")
    print(f"Версия PySide6: {PySide6.__version__}")
except ImportError as e:
    print(f"✗ Ошибка импорта: {e}")