# ui/menus/file/choosing_basics.py
"""
Выпадающее меню 'Выбрать основной аккаунт'.
Загружает имена из participants.enc и позволяет выбрать активного пользователя.
"""

from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import QSettings
from data.participants_manager import ParticipantsManager


class ChooseMainAccountMenu(QMenu):
    """Выпадающее меню для выбора основного аккаунта."""

    def __init__(self, parent=None):
        super().__init__("Выбрать основной аккаунт", parent)
        self.parent_window = parent
        self.manager = ParticipantsManager()
        self.current_account = None
        self.settings = QSettings("T-Invest", "T-Invest")  # Организация и приложение

        # Восстанавливаем последний выбранный аккаунт при старте
        saved_account = self.settings.value("last_selected_account", "")
        if saved_account and self.manager.name_exists(saved_account):
            self.current_account = saved_account
            self.parent_window.setWindowTitle(f"T-Invest — аккаунт: {saved_account}")
        else:
            self._update_window_title()  # Пустой заголовок, если нет аккаунта

        self.aboutToShow.connect(self._populate_menu)

    def _populate_menu(self):
        """Обновляет список участников при открытии меню."""
        self.clear()

        participants = self.manager.list_participants()

        # Если текущий аккаунт больше не существует — сбрасываем его
        if self.current_account and not self.manager.name_exists(self.current_account):
            self.current_account = None
            self.settings.remove("last_selected_account")  # Удаляем из настроек
            self._update_window_title()  # Обновляем заголовок

        if not participants:
            no_action = QAction("Нет сохранённых аккаунтов", self.parent())
            no_action.setEnabled(False)
            self.addAction(no_action)

            # Сбрасываем текущий аккаунт и обновляем заголовок
            if self.current_account:
                self.current_account = None
                self._update_window_title()

        else:
            for name in participants:
                action = QAction(name, self.parent())
                action.setCheckable(True)
                action.setChecked(name == self.current_account)
                action.triggered.connect(lambda checked, n=name: self._select_account(n))
                self.addAction(action)

    def _select_account(self, name: str):
        """Устанавливает выбранный аккаунт и сохраняет его в настройках."""
        self.current_account = name
        self.parent_window.setWindowTitle(f"T-Invest — аккаунт: {name}")
        self.settings.setValue("last_selected_account", name)  # Сохраняем
        print(f"✅ Основной аккаунт установлен: {name}")

        # Обновляем состояние меню "Файл"
        if hasattr(self.parent_window, 'file_menu') and self.parent_window.file_menu:
            self.parent_window.file_menu._update_menu_state()

    def _update_window_title(self, name=None):
        """Обновляет заголовок окна. Если имя не передано — убирает упоминание аккаунта."""
        if name:
            self.parent_window.setWindowTitle(f"T-Invest — аккаунт: {name}")
        else:
            self.parent_window.setWindowTitle("T-Invest")

    def get_current_account(self) -> str | None:
        """Возвращает текущий выбранный аккаунт."""
        return self.current_account
