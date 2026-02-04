from PySide6.QtGui import QActionGroup


class SettingsMenu:
    def __init__(self, menu_bar, parent):
        self.parent = parent
        self.menu = menu_bar.addMenu("Настройка")
        self._setup_actions()

    def _setup_actions(self):
        # Подменю "Тема"
        theme_menu = self.menu.addMenu("🎨 Тема")

        # Группа для выбора одной темы
        theme_group = QActionGroup(self.parent)
        theme_group.setExclusive(True)  # Только одна тема активна

        # Светлая тема
        light_action = theme_menu.addAction("☀️ Светлая")
        light_action.setCheckable(True)
        theme_group.addAction(light_action)

        # Тёмная тема
        dark_action = theme_menu.addAction("🌙 Тёмная")
        dark_action.setCheckable(True)
        theme_group.addAction(dark_action)

        # Устанавливаем светлую как активную по умолчанию
        light_action.setChecked(True)

        # Подключаем действия
        light_action.triggered.connect(lambda: self.parent.load_stylesheet("ui/styles/light.css"))
        dark_action.triggered.connect(lambda: self.parent.load_stylesheet("ui/styles/dark.css"))

        # Разделитель
        self.menu.addSeparator()

        # Остальные пункты
        self.menu.addAction("⚙️ Общие настройки")
        self.menu.addAction("⌨️ Горячие клавиши")
        self.menu.addAction("ℹ️ О программе")
