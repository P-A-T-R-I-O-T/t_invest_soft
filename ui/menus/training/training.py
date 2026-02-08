class TrainingMenu:
    def __init__(self, menu_bar, parent):
        self.menu = menu_bar.addMenu("Обучение")
        self._setup_actions()

    def _setup_actions(self):
        self.menu.addAction("Начать обучение")
        self.menu.addAction("Настройки обучения")
