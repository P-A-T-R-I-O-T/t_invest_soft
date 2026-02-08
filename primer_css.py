from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)
button = QPushButton("Test")
style = button.style()

# Узнать имя стиля (например, "Windows", "Fusion", "macOS")
print("Current style:", app.style().objectName())

# Получить размеры элементов
size = style.sizeFromContents(
    style.CT_PushButton,
    style.CMS_None,
    button.sizeHint(),
    button
)
print("Button size from style:", size)