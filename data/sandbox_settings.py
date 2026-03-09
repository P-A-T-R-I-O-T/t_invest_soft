# data/sandbox_settings.py

from t_tech.invest import Client
from t_tech.invest.constants import INVEST_GRPC_API_SANDBOX
from data.participants_manager import ParticipantsManager



class SandboxSettings:
    """
    Класс для работы с настройками песочницы и подключения к T‑Invest API (песочница).
    """

    def __init__(self):
        self.manager = ParticipantsManager()
        self.current_account = None
        self.client = None

    def set_current_account(self, account_name: str) -> bool:
        """
        Устанавливает текущий аккаунт для работы в песочнице.

        Args:
            account_name (str): имя аккаунта.

        Returns:
            bool: True, если аккаунт установлен успешно, иначе False.
        """
        if not self.manager.name_exists(account_name):
            print(f"❌ Ошибка: аккаунт '{account_name}' не найден.")
            return False

        participant = self.manager.get_participant_by_name(account_name)
        if not participant:
            print(f"❌ Ошибка: не удалось получить данные аккаунта '{account_name}'.")
            return False

        if not participant.get("is_sandbox", False):
            print(f"⚠️ Предупреждение: аккаунт '{account_name}' не помечен как песочница.")

        self.current_account = account_name
        print(f"✅ Текущий аккаунт для песочницы установлен: {account_name}")
        return True

    def connect_to_sandbox(self) -> bool:
        """
        Подключается к T‑Invest API в режиме песочницы, используя токен текущего аккаунта.

        Returns:
            bool: True при успешном подключении, иначе False.
        """
        if not self.current_account:
            print("❌ Ошибка: текущий аккаунт не установлен. Сначала вызовите set_current_account().")
            return False

        token = self.manager.get_token_by_name(self.current_account)
        if not token:
            print(f"❌ Ошибка: токен для аккаунта '{self.current_account}' не найден.")
            return False

        try:
            # Создаём клиент с указанием target для песочницы
            self.client = Client(token, target=INVEST_GRPC_API_SANDBOX)
            print(f"✅ Подключено к песочнице T‑Invest (аккаунт: {self.current_account})")
            return True
        except Exception as e:
            print(f"❌ Ошибка подключения к песочнице: {e}")
            self.client = None
            return False

    def get_accounts_list(self) -> list or None:
        """
        Получает список счетов для текущего аккаунта в песочнице.

        Returns:
            list or None: список счетов или None при ошибке.
        """
        if not self.client:
            print("❌ Ошибка: клиент не подключён. Сначала вызовите connect_to_sandbox().")
            return None

        try:
            with self.client as client:
                response = client.users.get_accounts()
                accounts = response.accounts
                print(f"📋 Получен список счетов для аккаунта '{self.current_account}':")
                for account in accounts:
                    print(f"  - {account.broker_account_id} ({account.status})")
                return accounts
        except Exception as e:
            print(f"❌ Ошибка при получении списка счетов: {e}")
            return None

    def disconnect(self):
        """
        Отключает клиента от API.
        """
        self.client = None
        print("🔌 Отключено от песочницы T‑Invest.")

    def is_connected(self) -> bool:
        """
        Проверяет, подключён ли клиент к API песочницы.

        Returns:
            bool: True, если подключён, иначе False.
        """
        return self.client is not None
