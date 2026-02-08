class TradeMenu:
    def __init__(self, menu_bar, parent):
        self.menu = menu_bar.addMenu("Торговля")
        self._setup_actions()

    def _setup_actions(self):
        self.menu.addAction("Открыть сделку")
        self.menu.addAction("Закрыть сделку")
        self.menu.addAction("История сделок")
